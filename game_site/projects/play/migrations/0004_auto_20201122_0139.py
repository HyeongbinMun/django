# Generated by Django 3.1.3 on 2020-11-21 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0003_auto_20201115_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]