# Generated by Django 2.1.3 on 2018-11-15 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('will_expire', models.NullBooleanField()),
                ('valid_from', models.DateField()),
                ('valid_to', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('url', models.URLField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_current', models.NullBooleanField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(blank=True, max_length=128, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('url', models.URLField(blank=True, null=True)),
                ('degree', models.CharField(blank=True, max_length=64, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_current', models.NullBooleanField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ManyToManyField(related_name='programs', to='resume.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('url', models.URLField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ManyToManyField(related_name='schools', to='resume.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ManyToManyField(related_name='skills', to='resume.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='program',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.School'),
        ),
        migrations.AddField(
            model_name='position',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Profile'),
        ),
        migrations.AddField(
            model_name='institution',
            name='profile',
            field=models.ManyToManyField(related_name='institutions', to='resume.Profile'),
        ),
        migrations.AddField(
            model_name='course',
            name='profile',
            field=models.ManyToManyField(related_name='courses', to='resume.Profile'),
        ),
        migrations.AddField(
            model_name='course',
            name='program',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='resume.Program'),
        ),
        migrations.AddField(
            model_name='company',
            name='profile',
            field=models.ManyToManyField(related_name='companies', to='resume.Profile'),
        ),
        migrations.AddField(
            model_name='certification',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Institution'),
        ),
        migrations.AddField(
            model_name='certification',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Profile'),
        ),
    ]
