# Generated by Django 3.1.5 on 2021-01-12 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0003_auto_20210111_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]