# tests/conftest.py
import pytest
from dynaconf import settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    """Fixture to force the use of the 'testing' environment for all tests."""
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")
