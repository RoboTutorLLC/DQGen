# Generated by Django 2.1 on 2019-04-17 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='conf_file',
            field=models.FileField(upload_to='./conf_file/'),
        ),
        migrations.AlterField(
            model_name='request',
            name='input_file',
            field=models.FileField(upload_to='./input_file'),
        ),
    ]