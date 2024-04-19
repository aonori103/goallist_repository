# Generated by Django 5.0.4 on 2024-04-15 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goallist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2024, 4, 15, 9, 18, 29, 132435, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='goals',
            name='upload_at',
            field=models.DateField(default=datetime.datetime(2024, 4, 15, 9, 18, 29, 133413, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2024, 4, 15, 9, 18, 29, 132435, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task_due',
            field=models.DateField(default=datetime.datetime(2024, 4, 15, 18, 18, 29, 133413)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='upload_at',
            field=models.DateField(default=datetime.datetime(2024, 4, 15, 9, 18, 29, 133413, tzinfo=datetime.timezone.utc)),
        ),
    ]