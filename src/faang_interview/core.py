"""Core data models for FAANG interview resources."""

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class ResourceType(str, Enum):
    """Type of resource."""

    BOOK = "book"
    VIDEO = "video"
    COURSE = "course"
    PLATFORM = "platform"
    ARTICLE = "article"
    REPOSITORY = "repository"
    TOOL = "tool"


class ResourceCategory(str, Enum):
    """Category of resource."""

    CODING = "coding"
    SYSTEM_DESIGN = "system_design"
    BEHAVIORAL = "behavioral"
    AI_ML = "ai_ml"
    DATA_STRUCTURES = "data_structures"
    ALGORITHMS = "algorithms"
    OOP = "oop"
    GENERAL = "general"


class DifficultyLevel(str, Enum):
    """Difficulty level of resource."""

    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


class Resource(BaseModel):
    """Model for an interview preparation resource."""

    title: str = Field(..., description="Title of the resource")
    description: str = Field(..., description="Description of the resource")
    url: str = Field(..., description="URL to the resource")
    resource_type: ResourceType = Field(..., description="Type of resource")
    category: ResourceCategory = Field(..., description="Category of resource")
    difficulty: Optional[DifficultyLevel] = Field(None, description="Difficulty level of resource")
    is_free: bool = Field(True, description="Whether the resource is free")
    price: Optional[str] = Field(None, description="Price if not free")
    rating: Optional[float] = Field(None, gt=0.0, le=5.0, description="User rating (0.1-5.0)")
    tags: list[str] = Field(default_factory=list, description="Tags for the resource")

    @field_validator("url")
    @classmethod
    def validate_url(cls, v: str) -> str:
        """Validate URL format."""
        if not v.startswith(("http://", "https://")):
            msg = "URL must start with http:// or https://"
            raise ValueError(msg)
        return v

    class Config:
        """Pydantic configuration."""

        json_schema_extra = {
            "example": {
                "title": "NeetCode 150",
                "description": "Curated list of 150 LeetCode problems",
                "url": "https://neetcode.io/",
                "resource_type": "platform",
                "category": "coding",
                "difficulty": "intermediate",
                "is_free": True,
                "rating": 4.9,
                "tags": ["leetcode", "problems", "video-solutions"],
            }
        }


class StudyPlan(BaseModel):
    """Model for a study plan."""

    name: str = Field(..., description="Name of the study plan")
    description: str = Field(..., description="Description of the study plan")
    duration_weeks: int = Field(..., gt=0, description="Duration in weeks")
    hours_per_day: float = Field(..., gt=0, le=24, description="Recommended hours per day")
    resources: list[Resource] = Field(default_factory=list, description="List of resources")

    class Config:
        """Pydantic configuration."""

        json_schema_extra = {
            "example": {
                "name": "FAANG Preparation - 16 Weeks",
                "description": "Complete preparation plan for FAANG interviews",
                "duration_weeks": 16,
                "hours_per_day": 4.0,
                "resources": [],
            }
        }
