# Generated by Django 4.0 on 2022-02-15 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_survivor_ammunition_survivor_food_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survivor',
            name='age',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='survivor',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='survivor',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
