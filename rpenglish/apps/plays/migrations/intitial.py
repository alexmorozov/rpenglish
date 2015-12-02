# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import colorful.fields
import uuid


class Migration(migrations.Migration):

    replaces = [(b'plays', '0001_initial'), (b'plays', '0002_auto_20151202_1305')]

    dependencies = [
        ('scripts', 'initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Play',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('step', models.CharField(db_index=True, max_length=50, choices=[(b'read_translation', b'read_translation'), (b'review_source', b'review_source')])),
                ('bit', models.ForeignKey(related_name='plays', to='scripts.Bit')),
            ],
        ),
        migrations.CreateModel(
            name='PlayStudents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', colorful.fields.RGBColorField()),
                ('play', models.ForeignKey(related_name='students', to='plays.Play')),
                ('user', models.ForeignKey(related_name='plays', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='play',
            name='bit',
        ),
        migrations.RemoveField(
            model_name='play',
            name='step',
        ),
        migrations.AddField(
            model_name='play',
            name='script',
            field=models.ForeignKey(related_name='plays', default=1, to='scripts.Script'),
            preserve_default=False,
        ),
    ]
