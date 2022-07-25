# Generated by Django 4.0.6 on 2022-07-25 19:33

import Accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_alter_users_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profile_picture',
            field=models.ImageField(blank=True, default='user_logo.png', null=True, upload_to=Accounts.models.image_file_name),
        ),
    ]
