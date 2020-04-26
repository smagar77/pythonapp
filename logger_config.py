import os
import logging.config

LOG_FILE_PATH = os.environ.get('LOG_FILE_PATH', '')


class LoggerConfig:
    dictConfig = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s",
                'short': {'format': '%(message)s'}
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },
            "file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "filename": os.path.join(LOG_FILE_PATH, "ad-base.log"),
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8"
            },
        },
        "loggers": {
            "api": {
                "level": "WARNING",
                "handlers": ["file_handler"],
                "propagate": "no"
            }
        },
        "root": {
            "level": "DEBUG",
            "handlers": ["console", "file_handler"]
        }
    }

logging.config.dictConfig(LoggerConfig.dictConfig)