#--coding: utf8--

import uuid

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import force_text

from colorful.fields import RGBColorField

from scripts.models import Bit, Script


class Play(models.Model):
    uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    script = models.ForeignKey(
        Script, related_name='plays')

    def __unicode__(self):
        return u'{users}: {bit}'.format(
            users=', '.join(s.user.username for s in self.students.all()),
            bit=force_text(self.bit))

    def get_absolute_url(self):
        return reverse('plays:pk', kwargs={'pk': str(self.pk)})

    def get_next_url(self, bit, step):
        if self.script.bits.last().pk == bit.pk:
            return None
        return reverse('plays:bit', kwargs={
            'pk': str(self.pk),
            'bit_pk': bit.get_next().pk,
        })


class PlayStudents(models.Model):
    play = models.ForeignKey(
        Play, related_name='students')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='plays')
    color = RGBColorField()
