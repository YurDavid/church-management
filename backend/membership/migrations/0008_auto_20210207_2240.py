# Generated by Django 3.1.5 on 2021-02-07 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("membership", "0007_auto_20210123_0209")]

    operations = [migrations.RenameField(model_name="member", old_name="email_address", new_name="email")]
