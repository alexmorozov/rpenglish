#--coding: utf8--

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

from adminsortable.models import Sortable
from durationfield.db.models.fields.duration import DurationField


class Script(models.Model):
    title = models.CharField(
        max_length=200)
    source_url = models.URLField(
        'source URL',
        blank=True)

    def __unicode__(self):
        return self.title


def next_bit_title():
    return u'Эпизод {}'.format(Bit.objects.count() + 1)


class Bit(Sortable):
    script = models.ForeignKey(
        Script, related_name='bits')
    title = models.CharField(
        max_length=100, blank=True,
        default=next_bit_title)

    def __unicode__(self):
        return u'{script.title}, {bit.title}'.format(
            script=self.script, bit=self)

    def get_next_url(self, play, step):
        all_steps = settings.PLAY_STEPS
        index = all_steps.index(step.codename)

        if index < len(all_steps) - 1:
            next_step = all_steps[index + 1]
            return reverse('plays:detail', kwargs={
                'pk': str(play.pk),
                'bit_pk': self.pk,
                'step': next_step
            })
        return None


class Line(Sortable):
    bit = models.ForeignKey(
        Bit, related_name='lines')
    character = models.CharField(
        max_length=50, db_index=True)
    text = models.CharField(
        max_length=1024)
    time = DurationField(
        blank=True, null=True)

    character_ru = models.CharField(
        u'персонаж',
        blank=True, max_length=50, db_index=True)
    text_ru = models.CharField(
        u'перевод',
        blank=True, max_length=1024, db_index=True)
