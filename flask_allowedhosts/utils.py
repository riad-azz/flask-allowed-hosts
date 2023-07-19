import socket

DEBUG = False


def get_real_host(client_ip: str):
    try:
        domain_name = socket.gethostbyaddr(client_ip)[0]
        return domain_name
    except Exception as e:
        return None


def debug_log(message: str):
    if DEBUG:
        print(message)
