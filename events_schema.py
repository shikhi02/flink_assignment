import json


def get_schema():
    """
    This function loads the schema of the events data.
    We can alter below mentioned events_schema.json file for any changes in schema in future.
    """
    with open('events_schema.json', 'r') as file:
        schema = json.load(file)
    return schema
