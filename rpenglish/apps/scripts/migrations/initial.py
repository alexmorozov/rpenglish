# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import durationfield.db.models.fields.duration
import scripts.models


class Migration(migrations.Migration):

    replaces = [(b'scripts', '0001_initial'), (b'scripts', '0002_auto_20151130_1620'), (b'scripts', '0003_bit_title'), (b'scripts', '0004_auto_20151201_1050'), (b'scripts', '0005_auto_20151201_1255')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.CharField(max_length=50, db_index=True)),
                ('text', models.CharField(max_length=1024)),
                ('time', durationfield.db.models.fields.duration.DurationField(null=True, blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('character_ru', models.CharField(db_index=True, max_length=50, verbose_name='\u043f\u0435\u0440\u0441\u043e\u043d\u0430\u0436', blank=True)),
                ('text_ru', models.CharField(db_index=True, max_length=50, verbose_name='\u043f\u0435\u0440\u0435\u0432\u043e\u0434', blank=True)),
                ('bit', models.ForeignKey(related_name='lines', to='scripts.Bit')),
            ],
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('source_url', models.URLField(verbose_name=b'source URL', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='bit',
            name='script',
            field=models.ForeignKey(related_name='bits', to='scripts.Script'),
        ),
        migrations.AlterModelOptions(
            name='bit',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='line',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='bit',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='line',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='bit',
            name='title',
            field=models.CharField(default=scripts.models.next_bit_title, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='line',
            name='text_ru',
            field=models.CharField(db_index=True, max_length=1024, verbose_name='\u043f\u0435\u0440\u0435\u0432\u043e\u0434', blank=True),
        ),
    ]
