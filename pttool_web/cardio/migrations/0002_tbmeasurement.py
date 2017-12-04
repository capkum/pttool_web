# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membercode', models.CharField(max_length=14)),
                ('rhr', models.CharField(blank=True, max_length=2, null=True)),
                ('e_mhr', models.CharField(blank=True, max_length=3, null=True)),
                ('vo2max', models.CharField(blank=True, max_length=2, null=True)),
                ('mhr', models.CharField(blank=True, max_length=3, null=True)),
                ('recovery', models.CharField(blank=True, max_length=1, null=True)),
                ('frequency', models.CharField(max_length=2)),
                ('intensity', models.CharField(max_length=6)),
                ('target_time', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('wt', models.IntegerField()),
                ('l1', models.CharField(max_length=10)),
                ('it', models.IntegerField()),
                ('repeat', models.IntegerField()),
                ('l2', models.CharField(max_length=10)),
                ('rt', models.IntegerField()),
                ('ct', models.IntegerField()),
                ('l3', models.CharField(max_length=10)),
                ('weight', models.CharField(blank=True, max_length=3, null=True)),
                ('insertdate', models.DateField(unique=True)),
                ('speed', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'TB_MEASUREMENT',
                'managed': False,
            },
        ),
    ]
