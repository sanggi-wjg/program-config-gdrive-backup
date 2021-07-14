from typing import Callable

from app.exceptions import brief_error
from app.logs import logger


def logger_catch_error(f: Callable):
    def wrapper(icon, item, *args, **kwargs):
        try:
            return f(icon, item, *args, **kwargs)
        except:
            logger.error(brief_error())

    return wrapper


# def change_state_able(f: Callable):
#     def wrapper(icon, item, *args, **kwargs):
#         state = not item.checked
#         setattr(item, '_checked', lambda s: state)
#         change_config(target = f"{item}:{NAME_IS_USE}", value = state)
#
#         logger.info(f"Change {item} to {state}")
#         return f(icon, item, *args, **kwargs)
#
#     return wrapper
