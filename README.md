# api_final_yatube
### Описание
API социальной сети для блогеров
### Технологии
- Python 3.7
- Django 2.2.19
- Django REST framework 3.12.4
### Запуск проекта в dev-режиме (Windows)
- Создайте и активируйте виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
``` 
- Выполните миграции:
```
python manage.py migrate
```
- Запустите проект:
```
python manage.py runserver
```
### Пример использования
- Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.
```
http://127.0.0.1:8000/api/v1/posts/
```
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
### Авторы
alexbulavkin, команда Яндекс.Практикум








