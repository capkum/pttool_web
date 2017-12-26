# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbmember',
            name='updateuser',
        ),
        migrations.AlterField(
            model_name='tbadminaccount',
            name='insertdate',
            field=models.DateField(auto_now_add=True, max_length=21),
        ),
        migrations.AlterField(
            model_name='tbadminaccount',
            name='updatedate',
            field=models.DateField(auto_now=True, max_length=21, null=True),
        ),
        migrations.AlterField(
            model_name='tbmeasurement',
            name='insertdate',
            field=models.DateTimeField(auto_now_add=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tbmember',
            name='insertdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tbmember',
            name='updatedate',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
