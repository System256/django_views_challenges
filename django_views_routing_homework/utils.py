import json
from json.decoder import JSONDecodeError
import re


def json_validator(data):
    try:
        json.loads(data)
        return True
    except (ValueError, JSONDecodeError) as error:
        print("invalid json: %s" % error)
        return False


def is_validate_full_name(full_name: str) -> bool:
    return full_name and 5 < len(full_name) < 256


def is_validate_email(email: str) -> bool:
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return bool(re.match(regex, email))    


def is_registered_from(registered_from: str) -> bool:
    return registered_from in ['website', 'mobile_app']


def is_validate_age(age: int) -> bool:
    return isinstance(age, int)