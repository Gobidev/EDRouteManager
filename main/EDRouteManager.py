from views.mainview import *
from views.inputview import *
from config.config import *


commander_name = get_commander_name()
if commander_name == "key not found in config":
    start_input_window()
else:
    start_main_window()
