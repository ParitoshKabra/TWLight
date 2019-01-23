# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-17 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_auto_20190107_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='lang',
            field=models.CharField(blank=True, choices=[('ar', '\u0627\u0644\u0639\u0631\u0628\u064a\u0629'), ('br', 'brezhoneg'), ('da', 'dansk'), ('de', 'Deutsch'), ('en', 'English'), ('fa', '\u0641\u0627\u0631\u0633\u06cc'), ('fi', 'suomi'), ('fr', 'fran\xe7ais'), ('hi', '\u0939\u093f\u0928\u094d\u0926\u0940'), ('ko', '\ud55c\uad6d\uc5b4'), ('mk', '\u043c\u0430\u043a\u0435\u0434\u043e\u043d\u0441\u043a\u0438'), ('mr', '\u092e\u0930\u093e\u0920\u0940'), ('my', '\u1019\u103c\u1014\u103a\u1019\u102c\u1018\u102c\u101e\u102c'), ('pt', 'portugu\xeas'), ('pt-br', 'portugu\xeas do Brasil'), ('ru', '\u0440\u0443\u0441\u0441\u043a\u0438\u0439'), ('sv', 'svenska'), ('ta', '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd'), ('tr', 'T\xfcrk\xe7e'), ('zh-hans', '\u4e2d\u6587\uff08\u7b80\u4f53\uff09'), ('zh-hant', '\u4e2d\u6587\uff08\u7e41\u9ad4\uff09')], help_text='Language', max_length=128, null=True),
        ),
    ]
