"""Test fastapi_celery."""
from src import fastapi_celery # noqa: F821


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(fastapi_celery.__name__, str) # noqa: F821
