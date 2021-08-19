import sys

try:
    from .local import *
except ImportError:
    from .common import *

# if 'test' in sys.argv:
#     from .tests import *


# Settings logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "\n==================== Log entry ====================\n"
                      "asctime: %(asctime)s\n"
                      "level  : %(levelname)s\n"
                      "pid    : %(process)d\n"
                      "thread : %(thread)d\n"
                      "message: %(message)s\n",
            'datefmt': '%Y-%m-%d %H:%M:%S %z',
        },
        'simple': {
            'format': "%(asctime)s %(levelname)s %(message)s\n\n"
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG' if DEBUG else 'ERROR',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(VAR_DIR, 'log', 'django.err'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
