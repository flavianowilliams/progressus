import environ

from progressus.settings.settings import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)
