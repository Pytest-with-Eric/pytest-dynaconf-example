import dynaconf  # noqa

ROOT_URLCONF = "django_app.urls"

settings = dynaconf.DjangoDynaconf(__name__)  # noqa
