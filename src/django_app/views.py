from django.http import JsonResponse
from dynaconf import settings as dynaconf_settings


def index(request):
    """Display the current configuration values."""
    return JsonResponse(
        {
            "environment": dynaconf_settings.current_env,
            "debug": dynaconf_settings.DEBUG,
            "database_url": dynaconf_settings.DATABASES["default"]["NAME"],
        }
    )
