# Generated by Django 5.1.1 on 2024-09-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='default_avatar.png', null=True, upload_to='avatars/'),
        ),
    ]
