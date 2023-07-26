import sys

# fmt: off
LOGGING: dict = {
    "version": 1,
    "formatters": {
        "custom": {
            "format": '[%(asctime)s] [%(levelname)s] in %(module)s pid: "%(message)s"',
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "custom",
            "stream": sys.stdout,
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "custom",
            "filename": "app.log",
        }
    },
    "loggers": {
        "waitress": {
            "level": "NOTSET",
            "propagate": True,
            }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "file"],
    },
}
# fmt: on
