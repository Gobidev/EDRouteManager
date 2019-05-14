

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
