"""
flask_allowed_hosts

This package provides functionality to enforce allowed hosts in a Flask application.
"""

from .allowed_hosts import AllowedHosts, limit_hosts

__all__ = ["AllowedHosts", "limit_hosts"]
