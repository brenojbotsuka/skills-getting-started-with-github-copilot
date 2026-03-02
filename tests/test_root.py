"""Tests for root endpoint using AAA (Arrange-Act-Assert) pattern."""

from fastapi.testclient import TestClient
from src.app import app


class TestRootEndpoint:
    """Test suite for root endpoint."""

    def test_root_redirects_to_static_html(self):
        """Test that GET / redirects to /static/index.html."""
        # Arrange
        client = TestClient(app)

        # Act
        response = client.get("/", follow_redirects=False)

        # Assert
        assert response.status_code == 307
        assert response.headers["location"] == "/static/index.html"

    def test_root_with_follow_redirects(self):
        """Test that following redirect from / leads to successful response."""
        # Arrange
        client = TestClient(app)

        # Act
        response = client.get("/", follow_redirects=True)

        # Assert
        assert response.status_code == 200
