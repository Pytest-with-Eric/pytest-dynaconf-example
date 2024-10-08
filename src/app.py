from config import settings


def get_database_url():
    return settings.DATABASE_URL


def is_debug_mode():
    return settings.DEBUG


if __name__ == "__main__":
    print(f"Database URL: {get_database_url()}")
    print(f"Debug Mode: {is_debug_mode()}")
