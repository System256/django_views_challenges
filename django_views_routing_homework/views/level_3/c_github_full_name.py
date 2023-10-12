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
from django_views_routing_homework.utils import get_github_name_by_username


def fetch_name_from_github_view(request: HttpRequest, github_username: str) -> JsonResponse: 
    name = get_github_name_by_username(github_username)
    content = {"name": name}
    status_code = 200

    if response.status_code == 404:
        content = {}
        status_code = 404
    if name is None:
        name = None 
    
    return JsonResponse(content, safe=False, status=status_code)
