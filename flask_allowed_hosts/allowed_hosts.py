# Flask modules
from flask import request, abort, Flask

# Other modules
import ipaddress
from functools import wraps
from typing import List, Callable, Union


class AllowedHosts:
    def __init__(self, app=None, allowed_hosts: Union[List[str], str] = None, on_denied: Callable = None):
        self.app = app
        self.debug = False
        self.on_denied = on_denied
        self.allowed_hosts = allowed_hosts
        self.exempted_routes = []
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        if self.on_denied is None:
            self.on_denied = app.config.get('IP_LIMITER_ON_DENIED', None)

        if self.allowed_hosts is None:
            self.allowed_hosts = app.config.get('IP_LIMITER_ALLOWED_HOSTS', None)

        self.debug = app.config.get('IP_LIMITER_DEBUG', False)

    @staticmethod
    def is_ip_in_network(ip: str, network: str) -> bool:
        try:
            return ipaddress.ip_address(ip) in ipaddress.ip_network(network)
        except ValueError:
            return False

    def debug_log(self, message: str):
        if self.debug:
            print(f"IPLimiter: {message}")

    def is_valid_host(self, allowed_hosts: Union[List[str], str]) -> bool:
        if not allowed_hosts or allowed_hosts == "*" or allowed_hosts == ["*"]:
            self.debug_log(f"All hosts are allowed, request was permitted: {allowed_hosts}")
            return True

        client_ip = request.remote_addr
        self.debug_log(f"Client IP: {client_ip}")

        for host in allowed_hosts:
            if self.is_ip_in_network(client_ip, host):
                self.debug_log("Valid Client IP, request was permitted")
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
