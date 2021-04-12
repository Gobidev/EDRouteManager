from config import *


def csv_to_list(filename):
    try:
        file = open(filename, "r")
        content = file.read()
    except:
        set_file_path("")
        return

    content = content.replace('"', "")

    table = []

    rows = content.split("\n")

    for i in range(len(rows)):
        columns = rows[i].split(",")
        table.append(columns)

    return table


def delete_first_row(table):
    try:
        del table[0]
    except:
        pass
    return table


def get_systems(table):

    systems = []
    try:
        for row in table:
            systems.append(row[0])
    except:
        pass
    return systems


def is_system_of_route(commander_system, route_systems):
    try:
        for route_system in route_systems:
            if route_system == commander_system:
                return True, route_systems.index(route_system)
        return False, False
    except:
        return False, False
