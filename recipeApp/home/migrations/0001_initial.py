# Generated by Django 4.2.3 on 2023-07-27 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recepies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recepie_name', models.CharField(max_length=100)),
                ('recepie_description', models.TextField(max_length=500)),
                ('recepie_image', models.ImageField(upload_to='recepie')),
            ],
        ),
    ]