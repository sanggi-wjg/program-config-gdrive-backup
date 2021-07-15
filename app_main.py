import platform

from app.tray import run_tray

if __name__ == '__main__':
    try:
        if platform.system() != 'Windows':
            raise OSError
    except Exception as e:
        raise OSError('Only use Windows') from e

    run_tray()
