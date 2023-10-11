import requests
import json
from json.decoder import JSONDecodeError
from faker import Faker


def json_validator(data: bytes) -> bool:
    try:
        json.loads(data)
        return True
    except (ValueError, JSONDecodeError) as error:
        print("invalid json: %s" % error)
        return False
    

def get_github_name_by_username(github_username: str) -> str:
    profile_url = f"https://api.github.com/users/{github_username}"
    response = requests.get(profile_url)
    json_to_object = json.loads(response.content)
    name = json_to_object.get("name")
    return name


def generate_text_by_length(text_length: int) -> str:
    faker = Faker()

    text_length = int(text_length)

    increased_text_length = text_length + 200

    generated_text = faker.text(int(increased_text_length))

    truncated_generated_text = generated_text[:text_length]

    return truncated_generated_text