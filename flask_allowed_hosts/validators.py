from typing import Any


class ConfigValidator:
    @staticmethod
    def validate_allowed_hosts(allowed_hosts: Any):
        if allowed_hosts is None:
            return allowed_hosts

        is_str = isinstance(allowed_hosts, str)
        is_list = isinstance(allowed_hosts, list)

        if not is_list and not is_str:
            raise ValueError("Allowed hosts should be a list of host names, IP addresses or '*'")

        if is_str and allowed_hosts != "*":
            raise ValueError("Allowed hosts should be a list of host names, IP addresses or '*'")

        if is_list and any(type(x) is not str for x in allowed_hosts):
            raise ValueError("Allowed hosts should be a list of strings representing host names or IP addresses or '*'")

        return allowed_hosts

    @staticmethod
    def validate_on_denied(on_denied: Any):
        if on_denied is None:
            return on_denied

        if not callable(on_denied):
            raise ValueError("on_denied should be a callable function")

        return on_denied
