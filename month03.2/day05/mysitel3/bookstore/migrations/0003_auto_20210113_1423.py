# Generated by Django 2.2.12 on 2021-01-13 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_auto_20210110_1742'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': '图书'},
        ),
    ]