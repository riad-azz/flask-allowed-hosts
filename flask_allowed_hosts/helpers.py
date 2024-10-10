# Flask modules
from flask import request


# Python modules
import re
import socket
import ipaddress
from typing import List

# Local modules
from flask_allowed_hosts.logger import AllowedHostsLogger


def get_remote_address() -> str:
    return request.remote_addr or "127.0.0.1"


def get_host_ips(host: str) -> List[str]:
    try:
        host = socket.gethostbyname_ex(host)
        AllowedHostsLogger.info(f"Host: {host}")
        host_ips = host[2]
        AllowedHostsLogger.info(f"Host IPs: {host_ips}")
        return host_ips
    except socket.gaierror:
        AllowedHostsLogger.error(f"get_host_ips error: {host}")
        return []


def is_local_host(host: str) -> bool:
    try:
        host_ip = socket.gethostbyname(host)
        return ipaddress.ip_address(host_ip).is_loopback
    except socket.gaierror:
        return False


def is_valid_cidr_network(address: str, strict: bool = False) -> bool:
    # Regex pattern match CIDR networks
    pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/(?:[0-9]|[1-2][0-9]|3[0-2]))'
    regex = re.compile(pattern)

    if not regex.fullmatch(address):
        return False

    try:
        ipaddress.ip_network(address, strict=strict)
        return True
    except ValueError:
        AllowedHostsLogger.error(f"is_valid_cidr_network error: {address}")
        return False


def get_host_type(host: str) -> str:
    if is_local_host(host):
        return "localhost"

    if is_valid_cidr_network(host):
        return "network"

    return "host"
