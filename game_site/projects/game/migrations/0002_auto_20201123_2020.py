# Generated by Django 3.1.3 on 2020-11-23 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_data',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_data',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
