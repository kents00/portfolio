# Generated by Django 4.0.5 on 2023-10-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_photo', models.ImageField(upload_to='media')),
                ('project_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.TextField(max_length=1000)),
                ('publish', models.DateTimeField(default='2023-10-07')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_photo', models.ImageField(upload_to='media')),
                ('company_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
    ]
