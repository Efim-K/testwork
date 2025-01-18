# Generated by Django 5.1.5 on 2025-01-18 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('model', models.CharField(blank='True', max_length=255, null='True', verbose_name='Модель')),
                ('release_date', models.DateField(blank='True', null='True', verbose_name='Дата выхода на рынок')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='SalesNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('network_type', models.CharField(choices=[('FA', 'Завод'), ('NW', 'Розничная сеть'), ('IE', 'Индивидуальный предприниматель')], default='FA', max_length=2, verbose_name='Тип сети продаж')),
                ('email', models.EmailField(blank='True', max_length=100, null='True', unique=True, verbose_name='Электронный адрес')),
                ('country', models.CharField(blank='True', max_length=100, null='True', verbose_name='Страна')),
                ('city', models.CharField(blank='True', max_length=100, null='True', verbose_name='Город')),
                ('street', models.CharField(blank='True', max_length=100, null='True', verbose_name='Улица')),
                ('house_number', models.CharField(blank='True', max_length=10, null='True', verbose_name='Номер дома')),
                ('debt', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Задолженность перед поставщиком')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('products', models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.SET_NULL, to='network.product', verbose_name='Продукты')),
                ('supplier', models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.SET_NULL, to='network.salesnetwork', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Сеть по продажам электроники',
                'verbose_name_plural': 'Сети по продажам электроники',
                'ordering': ['name'],
            },
        ),
    ]
