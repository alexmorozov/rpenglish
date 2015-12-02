#--coding: utf8--

from django.conf.urls import url

from .views import PlayView, canonicalize

patterns = dict(
    script=r'(?P<pk>[A-z0-9\-]+)',
    bit=r'(?P<bit_pk>\d+)',
    step=r'(?P<step>[A-z0-9_]+)',
)


urlpatterns = [
    url('^{p[script]}$'.format(p=patterns), canonicalize, name='play'),
    url('^{p[script]}/{p[bit]}$'.format(p=patterns), canonicalize, name='bit'),
    url('^{p[script]}/{p[bit]}/{p[step]}$'.format(p=patterns),
        PlayView.as_view(), name='detail'),
]
