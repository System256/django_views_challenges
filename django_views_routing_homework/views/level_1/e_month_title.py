from django.http import HttpResponse, HttpResponseNotFound, HttpRequest


"""
Вьюха get_month_title_view возвращает название месяца по его номеру. 
Вся логика работы должна происходить в функции get_month_title_by_number.

Задания:
    1. Напишите логику получения названия месяца по его номеру в функции get_month_title_by_number
    2. Если месяца по номеру нет, то должен возвращаться ответ типа HttpResponseNotFound c любым сообщением об ошибке
    3. Добавьте путь в файле urls.py, чтобы при открытии http://127.0.0.1:8000/month-title/тут номер месяца/ 
       вызывалась вьюха get_month_title_view. Например http://127.0.0.1:8000/month-title/3/ 
"""

months_dict = {
    1:  'Январь',
    2:  'Февраль',
    3:  'Март',
    4:  'Апрель',
    5:  'Май',
    6:  'Июнь',
    7:  'Июль',
    8:  'Август',
    9:  'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь'
}


def get_month_title_by_number(month_number: int) -> str:
    if month_number in months_dict:
        return months_dict[month_number]


def get_month_title_view(request: HttpRequest, month_number: int) -> HttpResponse:
    if get_month_title_by_number(month_number):
        return HttpResponse(get_month_title_by_number(month_number))
    else:  
        return HttpResponseNotFound('Месяца с таким номером не существует')
