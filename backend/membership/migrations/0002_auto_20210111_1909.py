# Generated by Django 3.1.5 on 2021-01-11 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("membership", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="ministry", name="name", field=models.CharField(max_length=150, unique=True)
        )
    ]
