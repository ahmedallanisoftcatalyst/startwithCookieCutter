# settings/local_pydanny.py
# to use this setting you must run:
# python manage.py runserver --settings=config.settings.local
from .local import *
# Set short cache timeout
CACHE_TIMEOUT = 30
