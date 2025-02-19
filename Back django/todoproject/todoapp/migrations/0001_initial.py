# Generated by Django 5.1.6 on 2025-02-18 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100, unique=True)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tododata', models.CharField(max_length=100)),
                ('Userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.user')),
            ],
        ),
    ]
