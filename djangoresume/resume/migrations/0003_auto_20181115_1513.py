# Generated by Django 2.1.3 on 2018-11-15 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20181115_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='program',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='resume.Program'),
        ),
    ]
