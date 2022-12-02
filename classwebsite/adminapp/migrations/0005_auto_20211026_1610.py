# Generated by Django 3.1.1 on 2021-10-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]