# Generated by Django 4.0.5 on 2023-02-09 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0008_rename_trait_name_trait_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trait',
            old_name='name',
            new_name='trait_name',
        ),
    ]
