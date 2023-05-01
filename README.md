# API для Yatube - социальной сети

## Описание

Проект - API для блог-платформы Yatube.
С его помощью можно смотреть и создавать посты,
писать комментарии и подписываться на авторов.

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```html
git@github.com:nikitagorelko/api_final_yatube.git
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```html
python3 -m venv env
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```html
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```html
python3 manage.py migrate
```

Запустить проект:

```html
python3 manage.py runserver
```
