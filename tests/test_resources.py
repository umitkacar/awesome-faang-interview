"""Tests for resources module."""

from faang_interview.core import ResourceCategory, ResourceType
from faang_interview.resources import (
    get_all_resources,
    get_free_resources,
    get_resources_by_category,
    get_resources_by_type,
)


class TestGetAllResources:
    """Tests for get_all_resources function."""

    def test_returns_list(self) -> None:
        """Test that get_all_resources returns a list."""
        resources = get_all_resources()
        assert isinstance(resources, list)

    def test_returns_non_empty(self) -> None:
        """Test that get_all_resources returns non-empty list."""
        resources = get_all_resources()
        assert len(resources) > 0

    def test_all_items_are_resources(self) -> None:
        """Test that all items are Resource instances."""
        from faang_interview.core import Resource

        resources = get_all_resources()
        assert all(isinstance(r, Resource) for r in resources)


class TestGetResourcesByCategory:
    """Tests for get_resources_by_category function."""

    def test_filters_by_coding_category(self) -> None:
        """Test filtering by coding category."""
        resources = get_resources_by_category(ResourceCategory.CODING)
        assert all(r.category == ResourceCategory.CODING for r in resources)
        assert len(resources) > 0

    def test_filters_by_system_design_category(self) -> None:
        """Test filtering by system design category."""
        resources = get_resources_by_category(ResourceCategory.SYSTEM_DESIGN)
        assert all(r.category == ResourceCategory.SYSTEM_DESIGN for r in resources)
        assert len(resources) > 0

    def test_filters_by_ai_ml_category(self) -> None:
        """Test filtering by AI/ML category."""
        resources = get_resources_by_category(ResourceCategory.AI_ML)
        assert all(r.category == ResourceCategory.AI_ML for r in resources)

    def test_all_categories_covered(self) -> None:
        """Test that get_all_resources equals sum of all categories."""
        all_resources = get_all_resources()
        categorized = []
        for category in ResourceCategory:
            categorized.extend(get_resources_by_category(category))
        assert len(all_resources) == len(categorized)


class TestGetResourcesByType:
    """Tests for get_resources_by_type function."""

    def test_filters_by_book_type(self) -> None:
        """Test filtering by book type."""
        resources = get_resources_by_type(ResourceType.BOOK)
        assert all(r.resource_type == ResourceType.BOOK for r in resources)

    def test_filters_by_video_type(self) -> None:
        """Test filtering by video type."""
        resources = get_resources_by_type(ResourceType.VIDEO)
        assert all(r.resource_type == ResourceType.VIDEO for r in resources)

    def test_filters_by_platform_type(self) -> None:
        """Test filtering by platform type."""
        resources = get_resources_by_type(ResourceType.PLATFORM)
        assert all(r.resource_type == ResourceType.PLATFORM for r in resources)


class TestGetFreeResources:
    """Tests for get_free_resources function."""

    def test_returns_only_free_resources(self) -> None:
        """Test that only free resources are returned."""
        resources = get_free_resources()
        assert all(r.is_free for r in resources)
        assert len(resources) > 0

    def test_some_resources_are_paid(self) -> None:
        """Test that some resources are paid (to validate the test)."""
        all_resources = get_all_resources()
        paid_resources = [r for r in all_resources if not r.is_free]
        assert len(paid_resources) > 0

    def test_free_plus_paid_equals_total(self) -> None:
        """Test that free + paid resources equal total resources."""
        all_resources = get_all_resources()
        free_resources = get_free_resources()
        paid_resources = [r for r in all_resources if not r.is_free]
        assert len(free_resources) + len(paid_resources) == len(all_resources)
