

def csv_to_list(filename):

    file = open(filename, "r")
    content = file.read()

    content = content.replace('"', "")

    table = []

    rows = content.split("\n")

    for i in range(len(rows)):
        columns = rows[i].split(",")
        table.append(columns)

    return table


def delete_first_row(table):
    del table[0]
    return table


def get_systems(table):

    systems = []

    for row in table:
        systems.append(row[0])

    return systems


def is_system_of_route(commander_system, route_systems):

    for route_system in route_systems:
        if route_system == commander_system:
            return True, route_systems.index(route_system)
    return False, False


# ------- only for testing purposes -------
# table = csv_to_list("example.csv")
# table = delete_first_row(table)
# systems = get_systems(table)
# print(is_system_of_route("Omega Sector VE-Q b5-15", systems))
