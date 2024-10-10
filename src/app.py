from dynaconf import settings


def get_database_url():
    """Returns the current DATABASE_URL based on the active environment."""
    return settings.DATABASE_URL


def is_debug_mode():
    """Returns whether DEBUG mode is enabled based on the active environment."""
    return settings.DEBUG


if __name__ == "__main__":
    print(get_database_url())
    print(is_debug_mode())
