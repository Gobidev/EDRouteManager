from utils.edsm import get_commander_system


config_filepath = "../config/config.yml"


def write_to_yaml(key, value):

    old_content = {}
    new_content = {}

    file = open(config_filepath, "r")
    content = file.readlines()
    lines = []

    # remove \n
    for i in content:
        i = i.replace("\n", "")
        lines.append(i)

    # convert content to dictionary
    for n in lines:
        content_list = n.split(": ")
        old_content[content_list[0]] = content_list[1]

    if key in old_content:
        new_content[key] = value
        del old_content[key]
    else:
        new_content[key] = value

    for f in old_content:
        new_content[f] = old_content[f]

    file.close()

    # actual writing
    new_file = open(config_filepath, "w")

    # creating new string
    final_string = ""
    for element in new_content:
        final_string += element
        final_string += ": "
        final_string += new_content[element]
        final_string += "\n"

    new_file.write(final_string)
    new_file.close()


def read_yaml(key):

    file_content = {}
    file = open(config_filepath, "r")
    content = file.readlines()
    lines = []

    # remove \n
    for i in content:
        i = i.replace("\n", "")
        lines.append(i)

    # convert content to dictionary
    for n in lines:
        content_list = n.split(": ")
        file_content[content_list[0]] = content_list[1]

    try:
        return file_content[key]
    except:
        return "key not found in config"


def set_commander_name(commander_name):
    write_to_yaml("commander_name", commander_name)


def get_commander_name():
    return read_yaml("commander_name")


def set_file_path(file_path):
    write_to_yaml("file_path", file_path)


def get_file_path():
    return read_yaml("file_path")


def refresh_current_system():
    # get commander_name
    commander_name = get_commander_name()
    if commander_name == "key not found in config":
        print("commander name not set")
        return

    system = get_commander_system(commander_name)

    # set system to config
    write_to_yaml("current_system", system)


def get_current_system():
    return read_yaml("current_system")
