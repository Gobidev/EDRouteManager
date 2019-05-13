from urllib.request import urlopen
import json


def get_commander_system(commander_name):

    # Get the dataset
    url = 'https://www.edsm.net/api-logs-v1/get-position?commanderName=' + commander_name
    response = urlopen(url)

    # Convert bytes to string type and string type to dict
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)

    try:
        final_string = json_obj['system']
    except:
        final_string = "Commander was not found in the database"

    return final_string


def is_known(commander_name):
    # Get the dataset
    url = 'https://www.edsm.net/api-logs-v1/get-position?commanderName=' + commander_name
    response = urlopen(url)

    # Convert bytes to string type and string type to dict
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)

    if json_obj['msg'] == "OK":
        return True
    else:
        return False
