# Generated by Django 5.1.5 on 2025-02-05 01:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_mgr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_mgr_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('details', models.TextField(blank=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Compleated'), (2, 'Cancelled')], default=0)),
                ('starts_on', models.DateTimeField(auto_now_add=True)),
                ('ends_on', models.DateTimeField(auto_now_add=True)),
                ('priority', models.IntegerField(choices=[(0, 'No'), (1, 'Low'), (2, 'Normal'), (3, 'Hi'), (4, 'unavoidable')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'ordering': ['starts_on'],
            },
        ),
    ]
