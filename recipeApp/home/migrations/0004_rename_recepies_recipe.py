# Generated by Django 4.2.3 on 2023-07-27 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_recepies_recepie_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='recepies',
            new_name='recipe',
        ),
    ]
