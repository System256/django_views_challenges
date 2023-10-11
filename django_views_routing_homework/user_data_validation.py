from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def is_validate_full_name_length(full_name: str) -> bool:
    return full_name and 5 < len(full_name) < 256


def is_validate_email(email: str) -> bool:
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def is_registered_in(registered_from: str) -> bool:
    return registered_from in ['website', 'mobile_app']


def is_validate_age_type_int(age: int) -> bool:
    return isinstance(age, int)