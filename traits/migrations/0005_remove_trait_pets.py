# Generated by Django 4.0.5 on 2023-02-09 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0004_trait_pets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trait',
            name='pets',
        ),
    ]