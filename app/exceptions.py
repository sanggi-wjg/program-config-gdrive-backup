import sys
import traceback


class BackupProgramError(Exception):
    pass


class ConfigValueIsNotExist(BackupProgramError):
    pass


class ConfigKeyError(BackupProgramError):
    pass


def brief_error():
    exc_type, exc_value, exc_tb = sys.exc_info()
    return "(Type) : {} | (Line) : {} | (Msg) : {}\n{}".format(exc_type.__name__, exc_tb.tb_lineno, exc_value, traceback.format_exc())
