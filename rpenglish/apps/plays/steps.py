#--coding: utf8--

import inspect
import re
import sys

import six

from django.core.urlresolvers import reverse


class StepMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        new_class = super(StepMetaclass, mcs).__new__(mcs, name, bases, attrs)

        codename = re.sub(r'([A-Z])', lambda m: '_' + m.group(0).lower(), name)
        new_class.codename = codename.strip('_')
        new_class.template_name = 'plays/steps/{codename}.html'.format(
            codename=new_class.codename)
        return new_class


class Step(six.with_metaclass(StepMetaclass, object)):
    def __init__(self, play, bit, request):
        self.play = play
        self.bit = bit
        self.request = request

    def get_context_data(self, **kwargs):
        return {}

    def get_next_url(self):
        # Without substeps
        return None


class ReviewSource(Step):
    description = u'Знакомство с источником'


class RoleRotationBase(Step):
    def __init__(self, play, bit, request):
        super(RoleRotationBase, self).__init__(play, bit, request)
        self.students = self.play.students.all()
        self.num_students = len(self.students)
        self.round = int(self.request.GET.get('round', 0))

    def get_context_data(self, **kwargs):
        context = super(RoleRotationBase, self).get_context_data(**kwargs)

        lines = []

        for i, line in enumerate(self.bit.lines.all()):
            line.student = self.students[(i + self.round) % self.num_students]
            line.next_student = self.students[(i + self.round + 1) % self.num_students]  # NOQA
            lines.append(line)

        context.update(lines=lines)
        return context

    def get_next_url(self):
        if self.round < self.num_students - 1:
            url = reverse('plays:detail', kwargs={
                'pk': str(self.play.pk),
                'bit_pk': self.bit.pk,
                'step': self.codename
            })

            return '{url}?round={round}'.format(url=url, round=self.round + 1)
        return None


class DirectTranslation(RoleRotationBase):
    description = u'Прямой перевод'


class ReverseTranslation(RoleRotationBase):
    description = u'Обратный перевод'


class RolePlay(RoleRotationBase):
    description = u'Чтение по ролям'


registry = dict()

for _, obj in inspect.getmembers(sys.modules[__name__]):
    try:
        if issubclass(obj, Step):
            registry[obj.codename] = obj
    except TypeError:
        pass
