from django.db import models


class Questions(models.Model):
    q_id = models.IntegerField(verbose_name='ID вопроса')
    question = models.CharField(verbose_name='Текст вопроса')
    answer = models.CharField(verbose_name='Текст ответа')
    created_at = models.CharField(verbose_name='Дата создания вопроса')


