# Generated by Django 3.2.9 on 2021-12-06 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='tempo_preparo',
        ),
    ]