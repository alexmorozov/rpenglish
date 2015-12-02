# --coding: utf8--

from rpenglish.settings.common import *  # NOQA

DEBUG = True
TEMPLATE_DEBUG = DEBUG

if not TEST:
    INSTALLED_APPS += ('debug_toolbar', )
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )


INTERNAL_IPS = ['192.168.1.%d' % num for num in xrange(1, 255)]


def custom_show_toolbar(request):
    return DEBUG

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': 'settings.dev.custom_show_toolbar',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(module)s: %(message)s'
        },
    },
    'require_debug_true': {
        '()': 'django.utils.log.RequireDebugTrue',
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'rpenglish': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

if TEST:
    # Радикально ускоряет фабрики пользователей.
    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )

    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

    INSTALLED_APPS += (
        'django_nose',
    )

HAML_LOADERS = ('hamlpy.template.loaders.HamlPyFilesystemLoader',
                'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',)
TEMPLATE_LOADERS = HAML_LOADERS + COMMON_TEMPLATE_LOADERS
