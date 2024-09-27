# Flask modules
from flask import request, abort, Flask

# Other modules
import socket
from functools import wraps
from typing import List, Callable, Union

LOCAL_HOST_VARIANTS = ('localhost', '127.0.0.1', '::1')


class AllowedHosts:
    def __init__(self, app=None, allowed_hosts: Union[List[str], str] = None, on_denied: Callable = None):
        self.app = app
        self.debug = False
        self.on_denied = on_denied
        self.allowed_hosts = allowed_hosts
        self.exempted_routes = []
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask, debug: bool = False):
        self.debug = app.config.get('ALLOWED_HOSTS_DEBUG', debug)

        if self.allowed_hosts is None:
            self.allowed_hosts = app.config.get('ALLOWED_HOSTS', None)

        if self.on_denied is None:
            self.on_denied = app.config.get('ALLOWED_HOSTS_ON_DENIED', None)

    def get_hostname_ips(self, host: str) -> List[str]:
        try:
            host = socket.gethostbyname_ex(host)
            self.debug_log(f"Host: {host}")
            host_ips = host[2]
            self.debug_log(f"Host IPs: {host_ips}")
            return host_ips
        except socket.gaierror:
            return []

    def is_real_hostname(self, host: str, client_ip: str) -> bool:
        host_ips = self.get_hostname_ips(host)
        return client_ip in host_ips

    @staticmethod
    def is_local_connection_allowed(host: str, client_ip: str) -> bool:
        return host in LOCAL_HOST_VARIANTS and client_ip in ('127.0.0.1', '::1', '::ffff:127.0.0.1')

    def debug_log(self, message: str):
        if self.debug:
            print(f"AllowedHosts -> {message}")

    def is_valid_host(self, allowed_hosts: Union[List[str], str]) -> bool:
        if not allowed_hosts or allowed_hosts in ("*", ["*"]):
            self.debug_log("All hosts are allowed, request was permitted.")
            return True

        client_ip = request.remote_addr
        self.debug_log(f"Client IP: {client_ip}")

        if isinstance(allowed_hosts, str):
            allowed_hosts = [allowed_hosts]

        for host in allowed_hosts:
            if self.is_local_connection_allowed(host, client_ip):
                self.debug_log("Localhost connection permitted")
                return True
            elif self.is_real_hostname(host, client_ip):
                self.debug_log("Valid hostname, request was permitted.")
                return True

        self.debug_log("Invalid Client IP, request was not permitted")
        return False

    def limit(self, allowed_hosts: Union[List[str], str] = None, on_denied: Callable = None):
        if allowed_hosts is None:
            allowed_hosts = self.allowed_hosts
        if on_denied is None:
            on_denied = self.on_denied

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if func.__name__ in self.exempted_routes:
                    self.debug_log(f"Route {func.__name__} is exempted")
                    return func(*args, **kwargs)

                if self.is_valid_host(allowed_hosts):
                    return func(*args, **kwargs)

                if callable(on_denied):
                    return on_denied(*args, **kwargs)
                else:
                    abort(403)

            return wrapper

        return decorator
