# Flask modules
from flask import request, abort

# Other modules
from functools import wraps
from flask_allowedhosts.utils import get_real_host, debug_log


def limit_hosts(allowed_hosts: list = None):
    if allowed_hosts is None:
        allowed_hosts = []

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not allowed_hosts:
                return func(*args, **kwargs)

            client_ip = request.remote_addr
            host_name = request.host.split(':')[0]
            debug_log(f"Client IP: {client_ip}")
            debug_log(f"Request HOST: {host_name}")

            # Check if request header HOST was modified
            if client_ip != host_name:
                # Obtain the real HOST
                host_name = get_real_host(client_ip)
                debug_log(f"Real HOST: {host_name}")

            if host_name and host_name in allowed_hosts:
                debug_log("Valid HOST, request was permitted")
                return func(*args, **kwargs)
            else:
                debug_log("Invalid HOST, falling back to Client IP check")

            # If the host_name is None then use the client_ip to check
            if client_ip in allowed_hosts:
                debug_log("Valid Client IP, request was permitted")
                return func(*args, **kwargs)
            else:
                # Abort request if all checks failed
                debug_log("Invalid Client IP, request was not permitted")
                abort(403)

        return wrapper

    return decorator
