# Generated by Django 3.1.4 on 2021-04-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='request_data',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='log',
            name='request_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
