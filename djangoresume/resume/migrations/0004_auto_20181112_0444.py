# Generated by Django 2.1.3 on 2018-11-12 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20181112_0437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
