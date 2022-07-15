import os

from progressus.settings.settings import *

ALLOWED_HOSTS = os.environ.setdefault('ALLOWED_HOSTS',['200.17.101.198', '127.0.0.1', '10.10.0.30'])
