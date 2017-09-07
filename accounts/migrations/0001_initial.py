# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 15:07
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='', max_length=32, verbose_name='Страна')),
                ('region', models.CharField(default='', max_length=128, verbose_name='Регион')),
                ('locality', models.CharField(default='', max_length=64, verbose_name='Населенный пункт')),
                ('street', models.CharField(default='', max_length=256, verbose_name='Улица')),
                ('building', models.CharField(default='', max_length=32, verbose_name='Дом, строение, корпус')),
                ('apartment', models.CharField(max_length=8, null=True, verbose_name='Квартира, комната')),
                ('zipcode', models.CharField(default='', max_length=8, verbose_name='Почтовый индекс')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('status', models.SmallIntegerField(default=0, verbose_name='Статус')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Address', verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
