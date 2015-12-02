#--coding: utf8--

import re

from django import template
from django.template.defaulttags import cycle
from django.utils.html import mark_safe
register = template.Library()


@register.inclusion_tag('includes/youtube_embed.html')
def source(bit):
    if not bit.script.source_url:
        return {}

    match = re.match(r'.*v=([A-z0-9]+).*', bit.script.source_url)
    if not match:
        return {}

    return dict(
        code=match.groups(0)[0],
        start=bit.lines.first().time.seconds,
        end=bit.lines.last().time.seconds + 7,
    )


@register.inclusion_tag('plays/includes/student_badge.html')
def student_badge(student):
    return dict(student=student)
