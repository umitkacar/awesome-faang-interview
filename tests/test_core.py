"""Tests for core models."""

import pytest
from pydantic import ValidationError

from faang_interview.core import (
    DifficultyLevel,
    Resource,
    ResourceCategory,
    ResourceType,
    StudyPlan,
)


class TestResource:
    """Tests for Resource model."""

    def test_resource_creation(self, sample_resource: Resource) -> None:
        """Test creating a valid resource."""
        assert sample_resource.title == "Test Resource"
        assert sample_resource.is_free is True
        assert sample_resource.rating == 4.5

    def test_resource_validation_invalid_rating(self) -> None:
        """Test that invalid rating raises validation error."""
        with pytest.raises(ValidationError):
            Resource(
                title="Test",
                description="Test",
                url="https://example.com",
                resource_type=ResourceType.COURSE,
                category=ResourceCategory.CODING,
                rating=6.0,  # Invalid: should be 0-5
            )

    def test_resource_validation_negative_rating(self) -> None:
        """Test that negative rating raises validation error."""
        with pytest.raises(ValidationError):
            Resource(
                title="Test",
                description="Test",
                url="https://example.com",
                resource_type=ResourceType.COURSE,
                category=ResourceCategory.CODING,
                rating=-1.0,  # Invalid: should be 0-5
            )

    def test_resource_tags_default(self) -> None:
        """Test that tags default to empty list."""
        resource = Resource(
            title="Test",
            description="Test",
            url="https://example.com",
            resource_type=ResourceType.COURSE,
            category=ResourceCategory.CODING,
        )
        assert resource.tags == []

    def test_resource_free_default(self) -> None:
        """Test that is_free defaults to True."""
        resource = Resource(
            title="Test",
            description="Test",
            url="https://example.com",
            resource_type=ResourceType.COURSE,
            category=ResourceCategory.CODING,
        )
        assert resource.is_free is True


class TestResourceType:
    """Tests for ResourceType enum."""

    def test_all_types_exist(self) -> None:
        """Test that all expected resource types exist."""
        expected_types = {"book", "video", "course", "platform", "article", "repository", "tool"}
        actual_types = {t.value for t in ResourceType}
        assert actual_types == expected_types


class TestResourceCategory:
    """Tests for ResourceCategory enum."""

    def test_all_categories_exist(self) -> None:
        """Test that all expected categories exist."""
        expected_categories = {
            "coding",
            "system_design",
            "behavioral",
            "ai_ml",
            "data_structures",
            "algorithms",
            "oop",
            "general",
        }
        actual_categories = {c.value for c in ResourceCategory}
        assert actual_categories == expected_categories


class TestDifficultyLevel:
    """Tests for DifficultyLevel enum."""

    def test_all_levels_exist(self) -> None:
        """Test that all expected difficulty levels exist."""
        expected_levels = {"beginner", "intermediate", "advanced", "expert"}
        actual_levels = {level.value for level in DifficultyLevel}
        assert actual_levels == expected_levels


class TestStudyPlan:
    """Tests for StudyPlan model."""

    def test_study_plan_creation(self) -> None:
        """Test creating a valid study plan."""
        plan = StudyPlan(
            name="Test Plan",
            description="A test study plan",
            duration_weeks=16,
            hours_per_day=4.0,
        )
        assert plan.name == "Test Plan"
        assert plan.duration_weeks == 16
        assert plan.hours_per_day == 4.0
        assert plan.resources == []

    def test_study_plan_with_resources(self, sample_resource: Resource) -> None:
        """Test study plan with resources."""
        plan = StudyPlan(
            name="Test Plan",
            description="A test study plan",
            duration_weeks=16,
            hours_per_day=4.0,
            resources=[sample_resource],
        )
        assert len(plan.resources) == 1
        assert plan.resources[0].title == "Test Resource"

    def test_study_plan_validation_negative_duration(self) -> None:
        """Test that negative duration raises validation error."""
        with pytest.raises(ValidationError):
            StudyPlan(
                name="Test Plan",
                description="Test",
                duration_weeks=0,  # Invalid: must be > 0
                hours_per_day=4.0,
            )

    def test_study_plan_validation_hours_too_high(self) -> None:
        """Test that hours > 24 raises validation error."""
        with pytest.raises(ValidationError):
            StudyPlan(
                name="Test Plan",
                description="Test",
                duration_weeks=16,
                hours_per_day=25.0,  # Invalid: must be <= 24
            )
