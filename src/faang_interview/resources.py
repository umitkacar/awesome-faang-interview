"""Resource database for FAANG interview preparation."""

from faang_interview.core import (
    DifficultyLevel,
    Resource,
    ResourceCategory,
    ResourceType,
)

# Sample resources - in a real application, this would come from a database or API
RESOURCES: list[Resource] = [
    # Coding Platforms
    Resource(
        title="NeetCode 150",
        description="Curated list of 150 LeetCode problems with video explanations",
        url="https://neetcode.io/",
        resource_type=ResourceType.PLATFORM,
        category=ResourceCategory.CODING,
        difficulty=DifficultyLevel.INTERMEDIATE,
        is_free=True,
        rating=4.9,
        tags=["leetcode", "problems", "video-solutions", "2025"],
    ),
    Resource(
        title="LeetCode Grind 75",
        description="Structured study plan with 75 essential problems",
        url="https://www.techinterviewhandbook.org/grind75",
        resource_type=ResourceType.PLATFORM,
        category=ResourceCategory.CODING,
        difficulty=DifficultyLevel.INTERMEDIATE,
        is_free=True,
        rating=4.8,
        tags=["leetcode", "study-plan", "structured"],
    ),
    Resource(
        title="AlgoExpert",
        description="160+ curated problems with video explanations",
        url="https://www.algoexpert.io/",
        resource_type=ResourceType.PLATFORM,
        category=ResourceCategory.CODING,
        difficulty=DifficultyLevel.INTERMEDIATE,
        is_free=False,
        price="$99/year",
        rating=4.7,
        tags=["problems", "video", "structured"],
    ),
    # Books
    Resource(
        title="Cracking the Coding Interview",
        description="189 programming problems and solutions - Still #1 for FAANG",
        url="https://www.amazon.com/dp/0984782850",
        resource_type=ResourceType.BOOK,
        category=ResourceCategory.CODING,
        difficulty=DifficultyLevel.INTERMEDIATE,
        is_free=False,
        price="$30-40",
        rating=4.8,
        tags=["classic", "problems", "gayle-mcdowell"],
    ),
    Resource(
        title="System Design Interview Vol. 1",
        description="An insider's guide to system design by Alex Xu",
        url="https://www.amazon.com/dp/B08CMF2CQF",
        resource_type=ResourceType.BOOK,
        category=ResourceCategory.SYSTEM_DESIGN,
        difficulty=DifficultyLevel.ADVANCED,
        is_free=False,
        price="$30-35",
        rating=4.9,
        tags=["system-design", "alex-xu", "diagrams"],
    ),
    # YouTube Channels
    Resource(
        title="NeetCode YouTube",
        description="360K+ subs, Google engineer, best LeetCode explanations",
        url="https://www.youtube.com/@NeetCode",
        resource_type=ResourceType.VIDEO,
        category=ResourceCategory.CODING,
        difficulty=DifficultyLevel.INTERMEDIATE,
        is_free=True,
        rating=4.9,
        tags=["youtube", "leetcode", "explanations"],
    ),
    Resource(
        title="ByteByteGo",
        description="Alex Xu's system design channel - 500K+ subscribers",
        url="https://www.youtube.com/@ByteByteGo",
        resource_type=ResourceType.VIDEO,
        category=ResourceCategory.SYSTEM_DESIGN,
        difficulty=DifficultyLevel.ADVANCED,
        is_free=True,
        rating=4.9,
        tags=["youtube", "system-design", "alex-xu"],
    ),
    # Courses
    Resource(
        title="Grokking the System Design Interview",
        description="Pattern-based approach to system design",
        url="https://www.designgurus.io/course/grokking-the-system-design-interview",
        resource_type=ResourceType.COURSE,
        category=ResourceCategory.SYSTEM_DESIGN,
        difficulty=DifficultyLevel.ADVANCED,
        is_free=False,
        price="$122/year",
        rating=4.7,
        tags=["course", "patterns", "interactive"],
    ),
    # AI/ML Resources
    Resource(
        title="Machine Learning Interviews GitHub",
        description="Comprehensive free guide for ML interviews",
        url="https://github.com/alirezadir/Machine-Learning-Interviews",
        resource_type=ResourceType.REPOSITORY,
        category=ResourceCategory.AI_ML,
        difficulty=DifficultyLevel.ADVANCED,
        is_free=True,
        rating=4.8,
        tags=["ml", "ai", "github", "free"],
    ),
    # Tools
    Resource(
        title="Big O Cheat Sheet",
        description="Time and space complexity reference",
        url="https://www.bigocheatsheet.com/",
        resource_type=ResourceType.TOOL,
        category=ResourceCategory.DATA_STRUCTURES,
        difficulty=DifficultyLevel.BEGINNER,
        is_free=True,
        rating=4.7,
        tags=["reference", "complexity", "cheatsheet"],
    ),
    Resource(
        title="VisuAlgo",
        description="Visualize data structures and algorithms",
        url="https://visualgo.net/",
        resource_type=ResourceType.TOOL,
        category=ResourceCategory.ALGORITHMS,
        difficulty=DifficultyLevel.BEGINNER,
        is_free=True,
        rating=4.8,
        tags=["visualization", "interactive", "learning"],
    ),
]


def get_all_resources() -> list[Resource]:
    """Get all resources.

    Returns:
        List of all resources
    """
    return RESOURCES


def get_resources_by_category(category: ResourceCategory) -> list[Resource]:
    """Get resources by category.

    Args:
        category: The category to filter by

    Returns:
        List of resources in the specified category
    """
    return [r for r in RESOURCES if r.category == category]


def get_resources_by_type(resource_type: ResourceType) -> list[Resource]:
    """Get resources by type.

    Args:
        resource_type: The type to filter by

    Returns:
        List of resources of the specified type
    """
    return [r for r in RESOURCES if r.resource_type == resource_type]


def get_free_resources() -> list[Resource]:
    """Get only free resources.

    Returns:
        List of free resources
    """
    return [r for r in RESOURCES if r.is_free]
