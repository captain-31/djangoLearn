from django.apps import AppConfig


# djangoLearn/apps.py

class DjangoLearnConfig(AppConfig):  # Our app config class
    name = 'djangoLearn'
    verbose_name = "djangoLearn"


# djangoLearn/__init__.py
default_app_config = 'djangoLearn.apps.DjangoLearnConfig'
