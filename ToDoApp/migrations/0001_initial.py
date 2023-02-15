# Generated by Django 3.0.8 on 2023-02-08 17:11

import ToDoApp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(default=ToDoApp.models.one_week_hence)),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToDoApp.ToDoList')),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
    ]
