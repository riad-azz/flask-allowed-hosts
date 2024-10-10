# Flask modules
from flask import abort, Flask

# Python modules
from functools import wraps
from typing import List, Callable, Union

# Local modules
from flask_allowed_hosts.helpers import get_remote_address
from flask_allowed_hosts.validators import ConfigValidator
from flask_allowed_hosts.permission_manager import PermissionManager


class AllowedHosts:

    def __init__(self, app=None, allowed_hosts: Union[List[str], str] = None, on_denied: Callable = None):
        # Configurations
        self.app = app
        self.on_denied = ConfigValidator.validate_on_denied(on_denied)
        self.allowed_hosts = ConfigValidator.validate_allowed_hosts(allowed_hosts)

        # Initialization
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        if self.allowed_hosts is None:
            allowed_hosts_config = app.config.get('ALLOWED_HOSTS', ["*"])
            self.allowed_hosts = ConfigValidator.validate_allowed_hosts(allowed_hosts_config)

        if self.on_denied is None:
            on_denied_config = app.config.get('ALLOWED_HOSTS_ON_DENIED', None)
            self.on_denied = ConfigValidator.validate_on_denied(on_denied_config)

    def limit(self, allowed_hosts: Union[List[str], str] = None, on_denied: Callable = None):
        if allowed_hosts is None:
            allowed_hosts = self.allowed_hosts
        else:
            allowed_hosts = ConfigValidator.validate_allowed_hosts(allowed_hosts)

        if on_denied is None:
            on_denied = self.on_denied
        else:
            on_denied = ConfigValidator.validate_on_denied(on_denied)

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                request_ip = get_remote_address()
                if PermissionManager.is_request_allowed(request_ip, allowed_hosts):
                    return func(*args, **kwargs)

                if callable(on_denied):
                    return on_denied(*args, **kwargs)
                else:
                    abort(403)

            return wrapper

        return decorator


# For backward compatibility

def limit_hosts(allowed_hosts: Union[List[str], str] = None, on_denied: Callable = None):
    on_denied = ConfigValidator.validate_on_denied(on_denied)
    allowed_hosts = ConfigValidator.validate_allowed_hosts(allowed_hosts)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request_ip = get_remote_address()
            if PermissionManager.is_request_allowed(request_ip, allowed_hosts):
                return func(*args, **kwargs)

            if callable(on_denied):
                return on_denied(*args, **kwargs)
            else:
                abort(403)

        return wrapper

    return decorator
