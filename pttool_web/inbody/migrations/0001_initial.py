# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbInbody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq', models.IntegerField()),
                ('membercode', models.CharField(max_length=14)),
                ('weight', models.TextField()),
                ('bonesheep', models.TextField()),
                ('fatsheep', models.TextField()),
                ('fatrate', models.TextField()),
                ('insertdate', models.DateField()),
            ],
            options={
                'db_table': 'TB_INBODY',
                'managed': True,
            },
        ),
    ]
