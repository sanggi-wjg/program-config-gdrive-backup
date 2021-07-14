import os

from app.settings import CONFIG_PATH, LOG_PATH
from app.decorators import logger_catch_error
from app.logs import logger


@logger_catch_error
def on_click_open_config(icon, item):
    open_windows_file(icon, CONFIG_PATH)


@logger_catch_error
def on_click_open_log(icon, item):
    open_windows_file(icon,LOG_PATH)


@logger_catch_error
def on_click_program_exit(icon, item):
    logger.info('Program Exit')
    icon.stop()


def open_windows_file(icon, path: str):
    if not os.path.exists(path):
        icon.notify(f"{path} is not exist")
        raise FileNotFoundError(f"{path} is not exist")

    path = os.path.realpath(path)
    os.startfile(path)
