import os

# Application
APP_VERSION = '0.0.1'
APP_NAME = 'Config-Backup'
USER_NAME = os.getlogin()

# Debug
DEBUG = True

# Base Dir
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Logger
LOG_PATH = os.path.join(BASE_DIR, f'{APP_NAME}.log')
LOG_FORMAT = '[%(levelname)s] [%(asctime)s] %(message)s'

# Data Dir
DATA_DIR = os.path.join(BASE_DIR, 'data')
# ICON_PATH = os.path.join(DATA_DIR, 'kimoz.ico')
ICON_PATH = os.path.join(DATA_DIR, 'nuuuuna.png')
CONFIG_PATH = os.path.join(BASE_DIR, 'config.json')

# Constants
NAME_TERMINUS = 'Terminus'
NAME_IS_USE = 'Is_use'
NAME_PATH = 'Path'

# Default Config
DEFAULT_CONFIG = {
    NAME_TERMINUS: {
        NAME_IS_USE: False,
        NAME_PATH  : f"C:\\Users\{USER_NAME}\AppData\Roaming\terminus\config.yaml"
    }
}
