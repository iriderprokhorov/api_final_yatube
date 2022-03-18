### API проекта Yatube:

Данный проект представляет API к сервису для публикации постов

В нем реализована возможность получения списков постов,комментариев и подписок


### Установка:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:iriderprokhorov/api_final_yatube.git
```

```
cd kittygram
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Примеры

1.Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.:

```
GET /api/v1/posts
```
Удачное выполнение

```
{

    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": 

[

        {}
    ]

}

```
2.Создание публикации:

```
POST /api/v1/posts
```
Удачное выполнение

{

    "text": "string",
    "image": "string",
    "group": 0

}

```