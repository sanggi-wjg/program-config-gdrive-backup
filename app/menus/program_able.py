from app.decorators import logger_catch_error
from app.logs import logger
from app.settings import NAME_IS_USE
from app.utils import change_config


@logger_catch_error
def on_click_program_able(icon, item):
    state = not item.checked
    setattr(item, '_checked', lambda s: state)
    change_config(target = f"{item}:{NAME_IS_USE}", value = state)

    logger.info(f"Change {item} to {state}")
