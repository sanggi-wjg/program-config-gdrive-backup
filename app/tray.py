import pystray
from pystray import Menu, MenuItem

from app.logs import logger
from app.menus.program_able import on_click_program_able
from app.menus.sub_menu import (
    on_click_open_config, on_click_open_log, on_click_program_exit
)
from app.settings import APP_NAME, NAME_IS_USE
from app.utils import load_icon, load_config


def get_backup_menus(config):
    logger.debug(config)
    items = []

    for name in config:
        items.append(
            MenuItem(
                name,
                on_click_program_able,
                checked = lambda item: config[name][NAME_IS_USE]
            )
        )

    program_menu = MenuItem('Backup', Menu(
        *tuple(items)
    ))
    return program_menu


def run_tray():
    logger.info('Program Start')
    CONFIG = load_config()

    icon = pystray.Icon(APP_NAME, load_icon())
    icon.menu = Menu(
        # Backup Target Menus
        get_backup_menus(CONFIG),
        # Submenus
        MenuItem(
            'Open Config',
            on_click_open_config
        ),
        MenuItem(
            'Open Log',
            on_click_open_log
        ),
        MenuItem(
            'Exit',
            on_click_program_exit
        )
    )
    icon.run()
