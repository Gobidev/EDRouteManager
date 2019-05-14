import json


def set_coommander_name(commander_name):
    config = {"commander_name": commander_name}
    with open("config.json", "w") as f:
        json.dump(config, f)


def get_commander_name():
    config = "commander_name"
    with open("config.json", "r") as f:
        return json.load(f)[config]
