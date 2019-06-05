from views.mainview import *
from utils.clipboard import *
from utils.csv_reader import *
import threading
import time

output = False


def loop_refresh(seconds=4):

    systems = None
    next_system = ""

    while 1:
        refresh_current_system()

        file_path = get_file_path()
        if output:
            print("file_path:", file_path)
        if not file_path == "key not found in config":
            if systems is None:
                table = csv_to_list(file_path)
                table = delete_first_row(table)
                systems = get_systems(table)
                if output:
                    print("systems:", systems)
            else:
                is_route_system, index = is_system_of_route(get_current_system(), systems)
                if output:
                    print("is_route_system:", is_route_system)
                    print("index:", index)
                if is_route_system:
                    try:
                        next_system = systems[index+1]
                    except:
                        systems = None
                        next_system = ""
                        time.sleep(10)
                else:
                    systems = None
                    time.sleep(10)

            copy_to_clipboard(next_system)

        set_info_content(get_commander_name(), get_current_system(), next_system)

        time.sleep(seconds)


commander_name = get_commander_name()

if commander_name == "key not found in config":
    threading.Thread(target=start_main_window).start()
    refresh_current_system()
else:
    threading.Thread(target=start_main_window).start()
    threading.Thread(target=loop_refresh).start()
