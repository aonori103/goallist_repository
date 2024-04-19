# Generated by Django 5.0.4 on 2024-04-15 09:17

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.datetime(2024, 4, 15, 18, 17, 6, 31323))),
                ('upload_at', models.DateField(default=datetime.datetime(2024, 4, 15, 18, 17, 6, 31323))),
                ('goal_title', models.CharField(max_length=100)),
                ('goal_detail', models.CharField(max_length=200)),
                ('goal_condition', models.IntegerField(default=False)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'goals',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.datetime(2024, 4, 15, 18, 17, 6, 31323))),
                ('upload_at', models.DateField(default=datetime.datetime(2024, 4, 15, 18, 17, 6, 31323))),
                ('task_title', models.CharField(max_length=100)),
                ('task_condition', models.IntegerField(default='0', max_length=3)),
                ('task_priority', models.IntegerField(default='0')),
                ('task_due', models.DateField(default=datetime.datetime(2024, 4, 15, 18, 17, 6, 31323))),
                ('goals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goallist.goals')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]