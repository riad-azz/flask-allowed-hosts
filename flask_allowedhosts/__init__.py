import warnings

from .decorators import limit_hosts

warnings.warn("flask_allowedhosts is deprecated, please use flask_allowed_hosts instead", DeprecationWarning)
