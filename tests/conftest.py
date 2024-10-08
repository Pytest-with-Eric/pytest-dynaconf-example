import pytest
from dynaconf import Dynaconf
from pathlib import Path

ROOT = Path(__file__).parent.parent


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    # Configure the settings for the testing environment and force it
    settings = Dynaconf(
        root_path=ROOT,
        envvar_prefix="DYNACONF",
        settings_files=["settings.toml", ".secrets.toml"],
        environments=True,
        FORCE_ENV_FOR_DYNACONF="testing",  # Force testing environment
    )
    return settings  # Return the settings object for use in tests
