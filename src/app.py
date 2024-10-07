from dynaconf import Dynaconf

# Load settings from settings.toml
settings = Dynaconf(
    settings_files=["settings.toml"],
    environments=True,
)


# Function to get the database URL
def get_database_url():
    return settings.DATABASE_URL


# Function to check if debug mode is enabled
def is_debug_mode():
    return settings.DEBUG


if __name__ == "__main__":
    # Print the current settings based on the environment
    print(f"Database URL: {get_database_url()}")
    print(f"Debug Mode: {is_debug_mode()}")
