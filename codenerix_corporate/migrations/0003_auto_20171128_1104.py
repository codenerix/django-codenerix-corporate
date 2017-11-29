# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-28 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_corporate', '0002_auto_20170724_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='corporateimage',
            name='address',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='corporateimage',
            name='city',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='corporateimage',
            name='email',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='corporateimage',
            name='phone',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Phone'),
        ),
        migrations.AddField(
            model_name='corporateimage',
            name='province',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Province'),
        ),
        migrations.AddField(
            model_name='corporateimage',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Zipcode'),
        ),
    ]
