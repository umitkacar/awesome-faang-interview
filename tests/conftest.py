"""Pytest configuration and fixtures."""

import pytest

from faang_interview.core import (
    DifficultyLevel,
    Resource,
    ResourceCategory,
    ResourceType,
)


@pytest.fixture
def sample_resource() -> Resource:
    """Create a sample resource for testing.

    Returns:
        A sample Resource instance
    """
    return Resource(
        title="Test Resource",
        description="A test resource for unit testing",
        url="https://example.com",
        resource_type=ResourceType.COURSE,
        category=ResourceCategory.CODING,
        difficulty=DifficultyLevel.INTERMEDIATE,
        is_free=True,
        rating=4.5,
        tags=["test", "example"],
    )


@pytest.fixture
def sample_resources() -> list[Resource]:
    """Create multiple sample resources for testing.

    Returns:
        A list of sample Resource instances
    """
    return [
        Resource(
            title="Free Coding Resource",
            description="A free coding resource",
            url="https://example.com/free",
            resource_type=ResourceType.COURSE,
            category=ResourceCategory.CODING,
            is_free=True,
            rating=4.5,
            tags=["free", "coding"],
        ),
        Resource(
            title="Paid System Design",
            description="A paid system design resource",
            url="https://example.com/paid",
            resource_type=ResourceType.BOOK,
            category=ResourceCategory.SYSTEM_DESIGN,
            is_free=False,
            price="$50",
            rating=4.8,
            tags=["paid", "system-design"],
        ),
        Resource(
            title="ML Video Course",
            description="Machine learning video course",
            url="https://example.com/ml",
            resource_type=ResourceType.VIDEO,
            category=ResourceCategory.AI_ML,
            is_free=True,
            rating=4.7,
            tags=["ml", "video", "free"],
        ),
    ]
