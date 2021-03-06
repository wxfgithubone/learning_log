# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-07-12 15:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning_logs', '0005_img2'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('st_name', models.CharField(max_length=25, verbose_name='学生姓名')),
                ('age', models.CharField(max_length=10, verbose_name='学生姓名')),
                ('sex', models.CharField(choices=[('男', '男'), ('女', '女'), ('性别不详', '性别不详')], default='性别不详', max_length=10, verbose_name='学生性别')),
                ('phone', models.CharField(error_messages={'unique': '手机号已存在'}, max_length=11, unique=True, verbose_name='手机号')),
                ('home', models.CharField(max_length=128, verbose_name='学生地址')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Img',
        ),
    ]
