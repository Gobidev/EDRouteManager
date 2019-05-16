from views.mainview import *
from views.inputview import *
from config.config import *
import threading
import time


def loop_refresh(seconds=7):
    refresh_current_system()
    time.sleep(seconds)


commander_name = get_commander_name()

if commander_name == "key not found in config":
    threading.Thread(target=start_input_window).start()
else:
    threading.Thread(target=start_main_window).start()
    refresh_current_system()
    set_info_content(get_commander_name(), get_current_system(), "")
    