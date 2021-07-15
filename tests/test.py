from app.tray import get_backup_menus
from app.utils import load_config

if __name__ == '__main__':
    get_backup_menus(
        load_config()
    )
