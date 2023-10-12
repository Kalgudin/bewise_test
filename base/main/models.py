from django.db import models


class CarModel(models.Model):
    brand = models.CharField(max_length=100, default='', verbose_name='Марка')
    model = models.CharField(max_length=100, default='', verbose_name='Модель')
    desc = models.CharField(max_length=1000, default='', verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')

    class Meta:
        verbose_name_plural = "Тестовая Модель"

    def __str__(self):
        return self.brand + '/' + self.model
