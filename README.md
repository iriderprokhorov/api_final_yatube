### API проекта Yatube:

Данный проект представляет API к сервису для публикации постов

В нем реализована возможность получения списков постов,комментариев и подписок

- Вся логика описана в приложении api.работает с моделью Post через ModelViewSet.
API  доступен только аутентифицированным пользователям.В проекте используется аутентификация по токену TokenAuthentication.
Аутентифицированный пользователь авторизован на изменение и удаление своего контента. в остальных случаях доступ предоставляется только для чтения. При попытке изменить чужие данные возвращается код ответа 403 Forbidden.

## Для взаимодействия с ресурсами используются такие эндпоинты:
- api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен
- api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост
- api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id
- api/v1/groups/ (GET): получаем список всех групп.
- api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id
- api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
- api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.

В ответ на запросы POST, PUT и PATCH API возвращает объект, который был добавлен или изменён.


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
