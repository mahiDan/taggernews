# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_submitter'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='age',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
