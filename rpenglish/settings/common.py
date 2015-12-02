# --coding: utf8--

import os
import sys


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def path(*a):
    return os.path.join(PROJECT_ROOT, *a)

# This trick allows to import apps without that prefixes
sys.path.insert(0, path('apps'))
sys.path.insert(0, path('lib'))
sys.path.insert(1, path('.'))

TEST = 'test' in sys.argv

ALLOWED_HOSTS = ['rpe.io']

ADMINS = [
    ('Alex Morozov', 'inductor2000@mail.ru')
]

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

MEDIA_ROOT = path('../media')
STATIC_ROOT = path('../../static')

STATICFILES_DIRS = (
    path('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'rpenglish.urls'
WSGI_APPLICATION = 'rpenglish.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'djangobower',
    'hamlpy',
    'pipeline',
    'lib',
    'adminsortable',
    'scripts',
    'plays',
)


HAML_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'hamlpy.template.loaders.HamlPyFilesystemLoader',
        'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',
    )),
)

COMMON_TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_LOADERS = HAML_LOADERS + COMMON_TEMPLATE_LOADERS
TEMPLATE_DIRS = (
    path('templates'),
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP  # NOQA

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

STATICFILES_FINDERS += (
    'djangobower.finders.BowerFinder',
)

BOWER_COMPONENTS_ROOT = path('static')
BOWER_INSTALLED_APPS = (
    'bootstrap#3.3.6',
)

PIPELINE_COMPILERS = (
    'lib.sass.SASSCCompiler',
    'pipeline.compilers.coffee.CoffeeScriptCompiler',
)


def sass_load_paths(*apps):
    """
    A helper to make cross-imports of scss files possible
    """
    return ' '.join('--include-path %s/static' % path(app)
                    for app in apps)

# The paths to scss directories with files which should have a possibility of
# importing each other.
PIPELINE_SASSC_ARGUMENTS = sass_load_paths('', )

PIPELINE_CSS_COMPRESSOR = None
PIPELINE_JS_COMPRESSOR = None
PIPELINE_DISABLE_WRAPPER = True

PIPELINE_CSS = {
    'base': {
        'source_filenames': [
            'bower_components/bootstrap/dist/css/bootstrap.css',
            'bower_components/bootstrap/dist/css/bootstrap-theme.css',
        ],
        'output_filename': 'css/base.css'
    }
}

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
STATICFILES_FINDERS += (
    'pipeline.finders.PipelineFinder',
)

# Параметры для удобного запуска ./manage.py shell_plus --notebook
IPYTHON_ARGUMENTS = [
    '--ext', 'django_extensions.management.notebook_extension',
]

NOTEBOOK_ARGUMENTS = [
    '--ip=0.0.0.0',
    '--no-browser',
]

STUDENT_COLORS = ['#ff0000', '#00ff00', '#0000ff', ]
PLAY_STEPS = ['review_source', 'direct_translation', 'reverse_translation',
              'role_play', ]
