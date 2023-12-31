# Generated by Django 4.2.1 on 2023-05-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_alter_userinfo_creat_time_alter_userinfo_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrettyNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=32, verbose_name='车牌号')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='价格')),
                ('level', models.IntegerField(choices=[(1, '一级'), (2, '二级'), (3, '三级'), (4, '四级')], default=1, verbose_name='级别')),
                ('status', models.SmallIntegerField(choices=[(1, '已用'), (2, '待用')], default=2, verbose_name='占用状态')),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别'),
        ),
    ]
