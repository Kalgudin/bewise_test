# Generated by Django 4.2.3 on 2023-07-25 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_testmodel_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='', max_length=100, verbose_name='Марка')),
                ('model', models.CharField(default='', max_length=100, verbose_name='Модель')),
                ('desc', models.CharField(default='', max_length=1000, verbose_name='Описание')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
            ],
        ),
    ]
