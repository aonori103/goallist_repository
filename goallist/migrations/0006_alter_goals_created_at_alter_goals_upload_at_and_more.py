# Generated by Django 5.0.4 on 2024-04-19 04:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goallist', '0005_alter_goals_created_at_alter_goals_goal_condition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 19, 13, 57, 53, 939829)),
        ),
        migrations.AlterField(
            model_name='goals',
            name='upload_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 19, 13, 57, 53, 939829)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 19, 13, 57, 53, 939829)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='upload_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 19, 13, 57, 53, 939829)),
        ),
        migrations.AlterModelTable(
            name='goals',
            table='goals',
        ),
    ]
