# Generated by Django 3.2.9 on 2021-12-06 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0005_receita_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y'),
        ),
    ]