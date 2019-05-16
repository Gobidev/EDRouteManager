from views.mainview import *
from views.inputview import *
from config.config import *
from utils.clipboard import *
from utils.csv_reader import *
import threading
import time


def loop_refresh(seconds=7):

    systems = None
    next_system = ""

    while 1:
        refresh_current_system()

        file_path = get_file_path()
        print("file_path:", file_path)
        if not file_path == "key not found in config":
            if systems is None:
                table = csv_to_list(file_path)
                table = delete_first_row(table)
                systems = get_systems(table)
                print("systems:", systems)
            else:
                is_system, index = is_system_of_route(get_current_system(), systems)
                print("is_system:", is_system)
                print("index:", index)
                if is_system:
                    next_system = systems[index+1]
                else:
                    next_system = systems[0]

        set_info_content(get_commander_name(), get_current_system(), next_system)
        copy_to_clipboard(next_system)

        time.sleep(seconds)


commander_name = get_commander_name()

if commander_name == "key not found in config":
    threading.Thread(target=start_input_window).start()
else:
    threading.Thread(target=start_main_window).start()
    threading.Thread(target=loop_refresh).start()
