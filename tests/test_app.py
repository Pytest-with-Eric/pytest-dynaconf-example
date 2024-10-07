from src.app import get_database_url


def test_database_url_testing_env():
    assert get_database_url() == "sqlite:///testing.db"
