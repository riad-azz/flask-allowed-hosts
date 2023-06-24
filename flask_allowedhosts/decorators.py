from functools import wraps
from flask import request, abort

def check_host(allowed_hosts: list = []):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(request.host)
            if not allowed_hosts:
                return func(*args, **kwargs)
            
            if request.host not in allowed_hosts:
                abort(403)
            
            return func(*args, **kwargs)
        return wrapper
    return decorator