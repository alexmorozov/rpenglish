#--coding: utf8--

import logging
import re

from django.core.management import BaseCommand

import pysrt

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help_text = 'Add the subtitles from a specified file to certain script'

    def add_arguments(self, parser):
            parser.add_argument('filename', type=str)

    def clean_text(self, text):
        return (text
                .replace('\n', ' ')
                .replace('. . .', '...')
                .replace('...', ''))

    def is_complete(self, text):
        return re.match(r'^.+?[\.\!\?]+\s*$', text)

    def group_subs(self, subs):
        lines = []
        start = []
        end = []
        for sub in subs:
            text = self.clean_text(sub.text)
            lines.append(text)
            start.append(sub.start)
            end.append(sub.end)

            if self.is_complete(text):
                yield (start[0], end[-1], ' '.join(lines))
                lines = []
                end = []
                start = []

    def handle(self, *args, **options):
        subs = self.group_subs(pysrt.open(options['filename']))
        print '\n'.join(s[2] for s in subs)
