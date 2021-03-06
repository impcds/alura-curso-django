# Generated by Django 3.2.9 on 2021-12-10 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receita', '0006_receita_foto_receita'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='id',
        ),
        migrations.AlterField(
            model_name='receita',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='receita',
            name='slug',
            field=models.SlugField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
