import logging
from typing import Any
from colorful_print import color

from app.settings import LOG_PATH, LOG_FORMAT
from app.utils import is_debug


class CustomLogger(logging.Logger):

    def debug(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        super().debug(msg, *args, **kwargs)
        print_debug(msg, *args, italic = True)

    def info(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        super().info(msg, *args, **kwargs)
        print_info(msg, *args)

    def warning(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        super().warning(msg, *args, **kwargs)
        print_warning(msg, *args, bold = True)

    def error(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        super().error(msg, *args, **kwargs)
        print_error(msg, *args, bold = True)


def colorful_dispatcher(c: str, msg: str, *args, **kwargs):
    if is_debug():
        dispatch = getattr(color, c)
        dispatch(msg, *args, **kwargs)


def print_debug(msg: str, *args, **kwargs):
    colorful_dispatcher('cyan', msg, *args, **kwargs)


def print_info(msg: str, *args, **kwargs):
    colorful_dispatcher('green', msg, *args, **kwargs)


def print_warning(msg: str, *args, **kwargs):
    colorful_dispatcher('yellow', msg, *args, **kwargs)


def print_error(msg: str, *args, **kwargs):
    colorful_dispatcher('red', msg, *args, **kwargs)


def create_logger():
    logging.setLoggerClass(CustomLogger)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG) if is_debug() else logger.setLevel(logging.INFO)

    handler = logging.FileHandler(LOG_PATH)
    handler.setFormatter(
        logging.Formatter(LOG_FORMAT)
    )
    logger.addHandler(handler)
    return logger


logger = create_logger()
