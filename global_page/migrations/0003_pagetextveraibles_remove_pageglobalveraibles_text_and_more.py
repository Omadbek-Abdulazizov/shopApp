# Generated by Django 4.2.7 on 2023-12-15 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_page', '0002_alter_pageglobalveraibles_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageTextVeraibles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='pageglobalveraibles',
            name='text',
        ),
        migrations.RemoveField(
            model_name='pageglobalveraibles',
            name='title',
        ),
    ]