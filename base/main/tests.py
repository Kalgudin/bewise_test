from django.test import TestCase
from .models import CarModel


class TestMain(TestCase):

    @classmethod
    def setUpTestData(cls):
        # try:
        #     test_web_base
        for n in range(10):
            CarModel.objects.create(brand=f"brand - { n }", model=f"model - { n }", desc=f"desc - { n }", price=100*n)

    def test_index(self):
        response = self.client.get('/')  # получаем ответ браузера
        self.assertEquals(response.status_code, 200)  # простая проверка кода ответа

    def test_main_contains(self):
        response = self.client.get('/')  # получаем ответ браузера
        self.assertIn('Main Page', response.content.decode())  # получаем контент в байтах и декодируем в строку

    def test_db_list(self):
        response = self.client.get('/db_list')
        self.assertEquals(response.status_code, 200)

    def test_db_list_contains(self):
        response = self.client.get('/db_list')
        self.assertIn('<h1>DB list</h1>', response.content.decode())

    def test_db_list_context(self):

        response = self.client.get('/db_list')
        self.assertIn("brand - 9", response.content.decode())







