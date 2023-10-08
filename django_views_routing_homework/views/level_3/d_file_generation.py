"""
В этом задании вам нужно научиться генерировать текст заданной длинны и возвращать его в ответе в виде файла.

- ручка должна получать длину генерируемого текста из get-параметра length;
- дальше вы должны сгенерировать случайный текст заданной длины. Это можно сделать и руками
  и с помощью сторонних библиотек, например, faker или lorem;
- дальше вы должны вернуть этот текст, но не в ответе, а в виде файла;
- если параметр length не указан или слишком большой, верните пустой ответ со статусом 403

Вот пример ручки, которая возвращает csv-файл: https://docs.djangoproject.com/en/4.2/howto/outputting-csv/
С текстовым всё похоже.

Для проверки используйте браузер: когда ручка правильно работает, при попытке зайти на неё, браузер должен
скачивать сгенерированный файл.
"""

from django.http import HttpResponse, HttpRequest, HttpResponseForbidden
import csv
import time
from faker import Faker


def generate_file_with_text_view(request: HttpRequest) -> HttpResponse:
    text_length = request.GET.get('length', 0)

    if not text_length or int(text_length) > 2000:
        return HttpResponseForbidden()

    faker = Faker()

    filename = f'generated_text_{time.strftime("%Y-%m-%d_%H-%M-%S")}_length_{text_length}.csv'

    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename={filename}'},
    )

    writer = csv.writer(response)
    writer.writerow([faker.text(int(text_length))])

    return response