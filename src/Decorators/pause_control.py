import asyncio, keyboard, threading, os
from dotenv import load_dotenv

load_dotenv('user_pref.env')
pauseKey = os.getenv('PAUSE') if os.getenv('PAUSE') is not None and os.getenv('PAUSE') != '' else 'f10'

pause_event = asyncio.Event()
pause_event.set()  # Começa como "não pausado"

def toggle_pause():
    if pause_event.is_set():
        print(f"⏸ Pausado. Pressione '{pauseKey}' novamente para continuar...")
        pause_event.clear()
    else:
        print("▶ Retomado.")
        pause_event.set()

def listen_for_key():
    keyboard.add_hotkey(pauseKey, toggle_pause)
    keyboard.wait()  # Mantém o thread ativo

def start_listener():
    thread = threading.Thread(target=listen_for_key, daemon=True)
    thread.start()