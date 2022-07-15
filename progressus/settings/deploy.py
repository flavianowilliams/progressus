import os
import environ

from progressus.settings import *

# Take environment variables from .env file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


env = environ.Env()

DEBUG = env.bool("DEBUG", True)

#environ['DEBUG'] = 'False'

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
