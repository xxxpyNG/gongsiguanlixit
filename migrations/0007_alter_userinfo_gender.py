# Generated by Django 4.2.1 on 2023-06-17 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别'),
        ),
    ]