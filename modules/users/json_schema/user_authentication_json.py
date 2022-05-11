from jsonschema import validate

json_user_authentication = {
    "title": "user_authentication",
    "type": "object",
    "required": ["user_name", "user_password"],
    "properties": {
        "user_name": {
            "type": "string"
        },
        "user_password": {
            "type": "string"
        }
    }
}


def json_validate_user_authentication(json):
    try:
        validate(json, json_user_authentication)
    except:
        return False
    return True
