"""
В этом задании вам нужно реализовать ручку, которая принимает на вход ник пользователя на Github,
а возвращает полное имя этого пользователя.

- имя пользователя вы узнаёте из урла
- используя АПИ Гитхаба, получите информацию об этом пользователе (это можно сделать тут: https://api.github.com/users/USERNAME)
- из ответа Гитхаба извлеките имя и верните его в теле ответа: `{"name": "Ilya Lebedev"}`
- если пользователя на Гитхабе нет, верните ответ с пустым телом и статусом 404
- если пользователь на Гитхабе есть, но имя у него не указано, верните None вместо имени
"""

from django.http import HttpRequest, JsonResponse
import requests
import json


def fetch_name_from_github_view(request: HttpRequest, github_username: str) -> JsonResponse:
    profile_url = f'https://api.github.com/users/{github_username}'
    response = requests.get(profile_url)
    json_to_object = json.loads(response.content)

    name = json_to_object.get("name", 0)

    content = {"name": name}
    status_code = 200

    if response.status_code == 404:
        content = {}
        status_code = 404
    if name is None:
        name = None 
    
    return JsonResponse(content, safe=False, status=status_code)
