import platform
from pystray import Menu, MenuItem

from app.logs import logger
from app.menus.program_able import on_click_program_able
from app.menus.sub_menu import (
    on_click_open_config, on_click_open_log, on_click_program_exit
)
from app.settings import APP_NAME, NAME_TERMINUS, NAME_IS_USE
from app.utils import load_icon, load_config


def run_tray():
    CONFIG = load_config()
    logger.info('Program Start')
    logger.debug(CONFIG)

    icon = pystray.Icon(APP_NAME, load_icon())
    icon.menu = Menu(
        MenuItem(
            'Program', Menu(
                MenuItem(
                    NAME_TERMINUS,
                    on_click_program_able,
                    checked = lambda item: CONFIG[NAME_TERMINUS][NAME_IS_USE],
                ),
            )),
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


if __name__ == '__main__':
    try:
        if platform.system() != 'Windows':
            raise OSError
    except Exception as e:
        raise OSError('Only use Windows') from e

    try:
        import pystray
    except ImportError as e:
        raise ImportError('Install pystray') from e

    run_tray()
