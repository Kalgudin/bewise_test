
text = """
    commands:
    - docker-compose build  # создаем образ
    - docker-compose run web python manage.py migrate  # выполняем миграции
    - docker-compose run web python manage.py createsuperuser  # создаем администратора(следуем инструкциям после выполнения комманды)
    - docker-compose up  # запускаем сервер
    
    
    
    """
print(text)
