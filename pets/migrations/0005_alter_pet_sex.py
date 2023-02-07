# Generated by Django 4.1.6 on 2023-02-07 11:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0004_alter_pet_sex"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="sex",
            field=models.CharField(
                choices=[
                    ("Male", "Male"),
                    ("Female", "Female"),
                    ("NotInformed", "Not Informed"),
                ],
                default="NotInformed",
                max_length=20,
            ),
        ),
    ]