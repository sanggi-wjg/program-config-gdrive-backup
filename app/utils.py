import json
import os

from PIL import Image

from app.exceptions import ConfigValueIsNotExist, ConfigKeyError
from app.settings import DEBUG, ICON_PATH, DEFAULT_CONFIG, CONFIG_PATH, APP_VERSION


def is_debug():
    return DEBUG


def load_icon():
    image = Image.open(ICON_PATH)
    return image


def get_version():
    return f"{APP_VERSION}"


def write_json(path: str = CONFIG_PATH, config: dict = None):
    if not config:
        raise ConfigValueIsNotExist

    with open(path, 'w') as f:
        f.write(json.dumps(config, indent = '\t'))


def load_config(path: str = CONFIG_PATH, target: str = None):
    if not os.path.exists(path):
        write_json(path, DEFAULT_CONFIG)

    with open(path, "r+") as f:
        config = json.load(f)

    if not target:
        return config
    else:
        try:
            target = target.split(':')
            return config[target[0]][target[1]]
        except KeyError:
            raise ConfigKeyError


def change_config(path: str = CONFIG_PATH, target: str = None, value = None):
    config = load_config()
    try:
        target = target.split(':')
        config[target[0]][target[1]] = value
    except KeyError:
        raise ConfigKeyError
    write_json(path, config)
