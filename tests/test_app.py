from src.app import get_database_url, is_debug_mode


def test_database_url_testing_env():
    assert get_database_url() == "sqlite:///testing.db"


def test_debug_mode_testing_env():
    assert is_debug_mode() is True
