# Generated by Django 2.0b1 on 2017-11-16 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0008_auto_20171116_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(default='', max_length=32, verbose_name='Название'),
        ),
    ]