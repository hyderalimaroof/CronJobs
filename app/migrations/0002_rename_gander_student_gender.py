# Generated by Django 4.0.3 on 2022-03-09 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='gander',
            new_name='gender',
        ),
    ]