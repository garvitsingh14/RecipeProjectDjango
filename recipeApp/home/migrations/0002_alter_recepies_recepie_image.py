# Generated by Django 4.2 on 2023-07-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recepies',
            name='recepie_image',
            field=models.ImageField(upload_to='recepie_images'),
        ),
    ]
