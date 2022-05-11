from jsonschema import validate

json_user_update = {
    "title": "user",
    "type": "object",
    "required": ["user_id", "user_name", "user_password", "user_email", "user_token", "user_status"],
    "properties": {
        "user_id": {
            "type": "integer"
        },
        "user_name": {
            "type": ["string", "null"]
        },
        "user_password": {
            "type": ["string", "null"]
        },
        "user_email": {
            "type": ["string", "null"]
        },
        "user_token": {
            "type": ["string", "null"]
        },
        "user_status": {
            "type": "integer",
            "enum": [0, 1]
        }
    }
}


def json_validate_update_user(json):
    try:
        validate(json, json_user_update)
    except Exception as e:
        print(e)
        return False
    return True