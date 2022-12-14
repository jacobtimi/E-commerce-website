# Generated by Django 3.1.1 on 2021-09-22 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_table',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('date_upload', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField(max_length=11)),
                ('description', models.CharField(max_length=100, null=True)),
                ('profile_picture', models.ImageField(unique=True, upload_to='product_image')),
                ('status', models.CharField(max_length=10, null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
