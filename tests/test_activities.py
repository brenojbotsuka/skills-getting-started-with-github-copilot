"""Tests for activities endpoint using AAA (Arrange-Act-Assert) pattern."""

from fastapi.testclient import TestClient
from src.app import app


class TestActivitiesEndpoint:
    """Test suite for activities endpoints."""

    def test_get_activities_returns_dict(self):
        """Test that GET /activities returns a dictionary of activities."""
        # Arrange
        client = TestClient(app)

        # Act
        response = client.get("/activities")

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert len(data) > 0

    def test_get_activities_contains_expected_fields(self):
        """Test that activities have expected fields."""
        # Arrange
        client = TestClient(app)

        # Act
        response = client.get("/activities")

        # Assert
        assert response.status_code == 200
        activities = response.json()
        # Verify activity structure: keys are names, values are dicts with details
        assert len(activities) > 0
        first_activity_name = list(activities.keys())[0]
        first_activity_details = activities[first_activity_name]
        
        assert isinstance(first_activity_name, str)
        assert isinstance(first_activity_details, dict)
        assert "description" in first_activity_details
        assert "schedule" in first_activity_details
        assert "max_participants" in first_activity_details
        assert "participants" in first_activity_details


class TestSignupEndpoint:
    """Test suite for signup endpoints."""

    def test_signup_for_activity_success(self):
        """Test successful signup for an activity."""
        # Arrange
        client = TestClient(app)
        response_activities = client.get("/activities")
        activities = response_activities.json()
        activity_name = list(activities.keys())[0]

        # Act
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": "test@example.com"}
        )

        # Assert
        assert response.status_code == 200

    def test_signup_for_nonexistent_activity(self):
        """Test signup for an activity that does not exist."""
        # Arrange
        client = TestClient(app)
        nonexistent_activity = "Nonexistent Activity 12345"

        # Act
        response = client.post(
            f"/activities/{nonexistent_activity}/signup",
            params={"email": "test@example.com"}
        )

        # Assert
        assert response.status_code == 404
