# Generated by Django 4.0.5 on 2023-02-09 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0012_pet_pets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='pets',
        ),
    ]
