from typing import Any


def raise_error_on_invalid_allowed_hosts(allowed_hosts: Any):
    if allowed_hosts is None:
        return

    is_str = isinstance(allowed_hosts, str)
    is_list = isinstance(allowed_hosts, list)

    if not is_list and not is_str:
        raise ValueError("Allowed hosts should be a list of host names, IP addresses or '*'")

    if is_str and allowed_hosts != "*":
        raise ValueError("Allowed hosts should be a list of host names, IP addresses or '*'")

    if is_list and any(type(x) is not str for x in allowed_hosts):
        raise ValueError("Allowed hosts should be a list of strings representing host names or IP addresses or '*'")


def raise_error_on_invalid_on_denied(on_denied: Any):
    if on_denied is None:
        return

    if not callable(on_denied):
        raise ValueError("on_denied should be a callable function")


def validate_limit_parameters(allowed_hosts: Any, on_denied: Any):
    raise_error_on_invalid_on_denied(on_denied)
    raise_error_on_invalid_allowed_hosts(allowed_hosts)
