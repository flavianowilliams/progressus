from os import environ
import environ

from progressus.settings.settings import *

env = environ.Env()

DEBUG = env.bool("DEBUG", True)

#environ['DEBUG'] = 'False'

#os.environ['ALLOWED_HOSTS'] = ['200.17.101.198', '127.0.0.1', '10.10.0.30']
