# Python modules
import re
import socket
import ipaddress
from typing import List, Union

# Local modules
from flask_allowed_hosts.helpers import get_host_ips, get_host_type

from flask_allowed_hosts.logger import AllowedHostsLogger


class PermissionManager:

    @staticmethod
    def _is_local_access_allowed(host: str, request_ip: str) -> bool:
        host_ip = socket.gethostbyname(host)
        if not ipaddress.ip_address(host_ip).is_loopback:
            return False

        return ipaddress.ip_address(request_ip).is_loopback

    @staticmethod
    def _is_network_access_allowed(address: str, request_ip: str, strict: bool = False) -> bool:
        try:
            ip_address = ipaddress.ip_address(request_ip)
            host_network = ipaddress.ip_network(address, strict=strict)
            network_range = host_network.num_addresses - 1
            AllowedHostsLogger.info(f"IP: {ip_address} - Network: {host_network} (range: {network_range})")

            return ip_address in host_network
        except Exception as e:
            AllowedHostsLogger.error(f"is_network_access_allowed error: {str(e)}")
            return False

    @staticmethod
    def _is_host_access_allowed(host: str, request_ip: str) -> bool:
        host_ips = get_host_ips(host)

        return request_ip in host_ips

    @classmethod
    def is_request_allowed(cls, request_ip: str, allowed_hosts: Union[List[str], str]) -> bool:
        if not allowed_hosts or allowed_hosts in ("*", ["*"]):
            AllowedHostsLogger.success("All hosts are allowed, request was permitted.")
            return True

        if isinstance(allowed_hosts, str):
            allowed_hosts = [allowed_hosts]

        AllowedHostsLogger.info(f"Request IP: {request_ip}")

        for host in allowed_hosts:
            host_type = get_host_type(host)

            AllowedHostsLogger.info(f"Host Type: {host_type}")

            if host_type == "localhost" and cls._is_local_access_allowed(host, request_ip):
                AllowedHostsLogger.success(f"Local Host request was permitted.")
                return True
            elif host_type == "network" and cls._is_network_access_allowed(host, request_ip):
                AllowedHostsLogger.success(f"Network Host request was permitted.")
                return True
            elif cls._is_host_access_allowed(host, request_ip):
                AllowedHostsLogger.success(f"Host request was permitted.")
                return True

        AllowedHostsLogger.custom("Invalid Host, request was not permitted", "🚫")
        return False
