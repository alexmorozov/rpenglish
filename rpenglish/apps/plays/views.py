from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views import generic

from .models import Play
from .steps import registry


def canonicalize(request, *args, **kwargs):
    play = Play.objects.get(pk=kwargs['pk'])
    bit_pk = kwargs.get('bit_pk', play.script.bits.first().pk)
    step = kwargs.get('step', settings.PLAY_STEPS[0])

    canonical_url = reverse('plays:detail',
                            kwargs=dict(
                                pk=str(play.pk),
                                bit_pk=bit_pk,
                                step=step))

    return redirect(canonical_url)


class PlayView(generic.DetailView):
    model = Play
    context_object_name = 'play'

    def get_next_url(self):
        candidates = [
            self.step.get_next_url(),
            self.bit.get_next_url(self.object, self.step),
            self.object.get_next_url(self.bit, self.step),
        ]
        try:
            return [url for url in candidates if url][0]
        except IndexError:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.bit = self.object.script.bits.get(pk=kwargs['bit_pk'])
        step_cls = registry[kwargs['step']]
        self.step = step_cls(self.object, self.bit, self.request)
        context = self.get_context_data(object=self.object,
                                        bit=self.bit,
                                        step=self.step,
                                        next_url=self.get_next_url(),
                                        **self.step.get_context_data())
        return self.render_to_response(context)
