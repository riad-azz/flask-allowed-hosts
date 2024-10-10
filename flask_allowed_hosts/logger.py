import os


class AllowedHostsLogger:
    DEBUG = os.environ.get("ALLOWED_HOSTS_DEBUG", "False") == "True"

    @classmethod
    def _print(cls, message: str, emoji: str = None) -> None:
        if not cls.DEBUG:
            return

        debug_message = "Flask Allowed Hosts -> " + message

        if emoji is not None:
            debug_message = f"{emoji}{debug_message}"

        print(debug_message)

    @classmethod
    def info(cls, message: str) -> None:
        cls._print(message, "🔍")

    @classmethod
    def error(cls, message: str) -> None:
        cls._print(message, "❌")

    @classmethod
    def warning(cls, message: str) -> None:
        cls._print(message, "⚠️")

    @classmethod
    def success(cls, message: str) -> None:
        cls._print(message, "✅")

    @classmethod
    def custom(cls, message: str, emoji: str) -> None:
        cls._print(message, emoji)
