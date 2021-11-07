import jsonschema
from jsonschema import validate
from events_schema import *


def validate_json(json_data):
    """
    This function validates the json_data with the events_schema that was created.
    Give result as true with a message if the input data matches the schema.
    Describe what kind of json you expect in event_schema module.
    """
    events_schema = get_schema()

    try:
        validate(instance=json_data, schema=events_schema)
    except jsonschema.exceptions.ValidationError as er:
        print(er)
        failure = "Given JSON data is InValid"
        print(failure)
        return False, failure

    success = "Given JSON data is Valid"
    return True, success
