# Generated by Django 2.1.3 on 2018-11-13 15:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]