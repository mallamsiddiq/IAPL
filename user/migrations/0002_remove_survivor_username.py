# Generated by Django 4.0 on 2022-02-15 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survivor',
            name='username',
        ),
    ]
