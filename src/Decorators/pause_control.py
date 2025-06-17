import asyncio, keyboard, threading, os
from functools import wraps
from dotenv import load_dotenv

load_dotenv('user_pref.env')
pauseKey = os.getenv('PAUSE') if os.getenv('PAUSE') is not None and os.getenv('PAUSE') != '' else 'f10'
# pauseKey = os.getenv('PAUSE') or 'f10'

paused = False
_listener_started = False

def start_pause_listener(pause_key=pauseKey):
    """_summary_

    Args:
        pause_key (_type_, optional): _description_. Defaults to pauseKey.
    """
    global _listener_started
    if _listener_started:
        return
    _listener_started = True

    def toggle():
        global paused
        paused = not paused
        print(f"\n[PAUSE] {'Pausado' if paused else 'Retomado'}")

    def listener():
        keyboard.add_hotkey(pause_key, toggle)
        keyboard.wait()

    threading.Thread(target=listener, daemon=True).start()

async def wait_if_paused():
    """_summary_
    """
    while paused:
        await asyncio.sleep(0.2)


def with_pause_control():
    """_summary_
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_pause_listener(pauseKey)
            return await func(*args, **kwargs)
        return wrapper
    return decorator

class PauseWrapper:
    """_summary_
    """
    def __init__(self, obj):
        """_summary_

        Args:
            obj (_type_): _description_
        """
        self._obj = obj

    def __getattr__(self, attr):
        """_summary_

        Args:
            attr (_type_): _description_

        Returns:
            _type_: _description_
        """
        original = getattr(self._obj, attr)

        if asyncio.iscoroutinefunction(original):
            async def wrapped(*args, **kwargs):
                await wait_if_paused()
                result = await original(*args, **kwargs)

                # Se o resultado for outro objeto Playwright (ex: Locator), embrulhar de novo
                if hasattr(result, '__class__') and 'playwright' in str(type(result)):
                    return PauseWrapper(result)
                return result
            return wrapped

        return original