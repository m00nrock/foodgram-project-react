# Foodgram
Стек технологий: Python 3, Django, REST API

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![Postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
  
### Как запустить проект:  

#### 1. для разработки:  
Клонировать репозиторий и перейти в него в командной строке:  
  
```shell
git clone https://github.com/m00nrock/foodgram-project-react.git
```

Заполнените .env файл:
В директории /infra/ создайте .env файл и укажите значения для переменных окружения:
Пример заполнения доступен в файле .env.example

- SECRET_KEY
- HOSTS
- DB_ENGINE
- DB_NAME
- POSTGRES_USER
- POSTGRES_PASSWORD
- DB_HOST
- DB_PORT

Дальнейшие действия выполняются в директории django проекта /backend/foodgram
Создать и активировать виртуальное окружение: 
  
```shell
python -m venv venv  
```
  
```shell
source venv/bin/activate  
```
  
```shell
python -m pip install --upgrade pip  
```
  
Установить зависимости из файла requirements.txt:  
  
```shell
pip install -r requirements.txt  
```
  
Выполнить миграции:  
  
```shell
python manage.py migrate  
```

Запустить проект:  
  
```shell
python manage.py runserver  
```
