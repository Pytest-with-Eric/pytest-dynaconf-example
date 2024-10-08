from src.app import get_database_url, is_debug_mode


def test_database_url_testing_env():
    """Test to verify that the DATABASE_URL from the 'testing' environment is used."""
    assert get_database_url() == "sqlite:///testing.db"


def test_debug_mode_testing_env():
    """Test to verify that DEBUG is True in the 'testing' environment."""
    assert is_debug_mode() is True
