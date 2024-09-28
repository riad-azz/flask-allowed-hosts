import os
import socket

from typing import List, Union

DEBUG = os.environ.get("ALLOWED_HOSTS_DEBUG", False)
LOCAL_HOST_VARIANTS = ('localhost', '127.0.0.1', '::1')


def debug_log(message: str):
    if DEBUG:
        print(f"Flask Allowed Hosts -> {message}")


def get_hostname_ips(host: str) -> List[str]:
    try:
        host = socket.gethostbyname_ex(host)
        debug_log(f"Host: {host}")
        host_ips = host[2]
        debug_log(f"Host IPs: {host_ips}")
        return host_ips
    except socket.gaierror:
        debug_log(f"get_hostname_ips error: {host}")
        return []


def is_real_hostname(host: str, request_ip: str) -> bool:
    host_ips = get_hostname_ips(host)
    return request_ip in host_ips


def is_local_connection_allowed(host: str, client_ip: str) -> bool:
    return host in LOCAL_HOST_VARIANTS and client_ip in ('127.0.0.1', '::1', '::ffff:127.0.0.1')


def is_valid_host(request_ip: str, allowed_hosts: Union[List[str], str]) -> bool:
    if not allowed_hosts or allowed_hosts in ("*", ["*"]):
        debug_log("All hosts are allowed, request was permitted.")
        return True

    if isinstance(allowed_hosts, str):
        allowed_hosts = [allowed_hosts]

    debug_log(f"Request IP: {request_ip}")

    for host in allowed_hosts:
        if is_local_connection_allowed(host, request_ip):
            debug_log("Localhost connection permitted")
            return True
        elif is_real_hostname(host, request_ip):
            debug_log("Valid Host, request was permitted.")
            return True

    debug_log("Invalid Host, request was not permitted")
    return False
