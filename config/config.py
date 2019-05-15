import json
from utils.edsm import get_commander_system

config_filepath = "..\config\config.json"


def set_commander_name(commander_name):
    config = {"commander_name": commander_name}
    with open(config_filepath, "w") as f:
        json.dump(config, f)
        print("set commander_name to", commander_name)


def get_commander_name():
    config = "commander_name"
    with open(config_filepath, "r") as f:
        return json.load(f)[config]


def set_file_path(file_path):
    config = {"file_path": file_path}
    with open(config_filepath, "w") as f:
        json.dump(config, f)
        print("set file_path to", file_path)


def get_file_path():
    config = "file_path"
    with open(config_filepath, "r") as f:
        return json.load(f)[config]


def refresh_current_system():
    # get commander_name
    try:
        commander_name = get_commander_name()
    except:
        print("commander name not set")
        return
    system = get_commander_system(commander_name)
    # set system to config
    config = {"current_system": system}
    with open(config_filepath, "w") as f:
        json.dump(config, f)
        print("set current_system to", system)
