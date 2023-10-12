# Bewise test job



## Getting started
Чтобы запустить контейнер на своем компьютере, в командной строке проекта выполните следующие команды:
```
    - docker-compose build
    - docker-compose run web python manage.py makemigrations  
    - docker-compose run web python manage.py migrate
    - docker-compose run web python manage.py createsuperuser
    - docker-compose up
```

Далее переходим в браузер и запускаем тестовый сервер.
```
   - http://127.0.0.1:8000
```

Так-же можно отправить Get-запрос напрямую к API по шаблону:
requests.post(http://127.0.0.1:8000/api/v1/questions', data={"questions_num": 1})

