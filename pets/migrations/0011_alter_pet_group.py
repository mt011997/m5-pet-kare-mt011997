# Generated by Django 4.0.5 on 2023-02-09 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_alter_group_created_at'),
        ('pets', '0010_alter_pet_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pets', to='groups.group'),
        ),
    ]