# Generated by Django 2.1.3 on 2018-11-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_school_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='order_id',
            field=models.PositiveIntegerField(default=1),
        ),
    ]