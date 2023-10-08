"""
В этом задании вам нужно реализовать вьюху, которая валидирует данные о пользователе.

- получите json из тела запроса
- проверьте, что данные удовлетворяют нужным требованиям
- если удовлетворяют, то верните ответ со статусом 200 и телом `{"is_valid": true}`
- если нет, то верните ответ со статусом 200 и телом `{"is_valid": false}`
- если в теле запроса невалидный json, вернуть bad request

Условия, которым должны удовлетворять данные:
- есть поле full_name, в нём хранится строка от 5 до 256 символов
- есть поле email, в нём хранится строка, похожая на емейл
- есть поле registered_from, в нём одно из двух значений: website или mobile_app
- поле age необязательное: может быть, а может не быть. Если есть, то в нём хранится целое число
- других полей нет

Для тестирования рекомендую использовать Postman.
Когда будете писать код, не забывайте о читаемости, поддерживаемости и модульности.
"""
from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest
import json
from django_views_routing_homework.utils import (
    json_validator,
    is_validate_full_name,
    is_validate_email,
    is_registered_from,
    is_validate_age,
)
    

def validate_user_data_view(request: HttpRequest) -> JsonResponse | HttpResponseBadRequest:
    if not json_validator(request.body):
        return HttpResponseBadRequest()
    
    data = dict(json.loads(request.body))
    
    full_name = data.get('full_name', 0)
    email = data.get('email', 0)
    registered_from = data.get('registered_from', 0)
    age = data.get('age', 0)

    checks = [
        is_validate_full_name(full_name),
        is_validate_email(email),
        is_registered_from(registered_from),
        is_validate_age(age)
    ]

    response = "{'is_valid': true}" if all(checks) else "{'is_valid': false}"
        
    return JsonResponse(data=response, status=200, safe=False)
