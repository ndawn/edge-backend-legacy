# Generated by Django 2.0.2 on 2018-05-06 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('previews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preview',
            name='mode',
            field=models.CharField(choices=[('weekly', 'Неделя'), ('monthly', 'Месяц')], max_length=8, null=True, verbose_name='Тип'),
        ),
    ]