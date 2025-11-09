# 🤝 Contributing to Awesome FAANG Interview Resources

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Development Workflow](#development-workflow)
- [Code Quality](#code-quality)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Adding New Resources](#adding-new-resources)

## 📜 Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code. Please be respectful and constructive in all interactions.

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- [Hatch](https://hatch.pypa.io/) (recommended) or pip

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/YOUR_USERNAME/awesome-faang-interview.git
cd awesome-faang-interview
```

3. Add the original repository as upstream:

```bash
git remote add upstream https://github.com/umitkacar/awesome-faang-interview.git
```

## 🛠️ Development Setup

### Option 1: Using Hatch (Recommended)

```bash
# Install Hatch
pip install hatch

# Hatch will automatically create and manage virtual environments
# Run tests
hatch run test

# Run all checks
hatch run all
```

### Option 2: Using pip and venv

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate

# Install development dependencies
pip install -e ".[dev]"
```

### Install Pre-commit Hooks

```bash
pre-commit install
```

This will run code quality checks automatically before each commit.

## 🔄 Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 2. Make Your Changes

- Write clean, readable code
- Follow the existing code style
- Add tests for new features
- Update documentation as needed

### 3. Run Quality Checks

```bash
# Format code
hatch run format

# Run linter
hatch run lint

# Run type checker
hatch run type-check

# Run tests
hatch run test

# Run all checks
hatch run all
```

### 4. Commit Your Changes

```bash
git add .
git commit -m "feat: add new feature"
```

**Commit Message Format:**

We use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

## ✨ Code Quality

### Code Style

- **Formatter:** [Black](https://github.com/psf/black) (line length: 100)
- **Linter:** [Ruff](https://github.com/astral-sh/ruff) (comprehensive linting)
- **Type Checker:** [MyPy](https://mypy-lang.org/) (strict mode)

### Pre-commit Hooks

We use pre-commit hooks to ensure code quality:

- ✅ Black - Code formatting
- ✅ Ruff - Linting and auto-fixes
- ✅ MyPy - Type checking
- ✅ Trailing whitespace removal
- ✅ YAML/JSON validation
- ✅ Security checks with Bandit
- ✅ And more!

### Manual Quality Checks

```bash
# Format code with Black
black src tests

# Lint with Ruff
ruff check src tests --fix

# Type check with MyPy
mypy src tests

# Run all quality checks
hatch run all
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
hatch run test

# Run with coverage
hatch run test-cov

# Run specific test file
pytest tests/test_core.py

# Run specific test
pytest tests/test_core.py::TestResource::test_resource_creation

# Run with verbose output
pytest -v

# Run and show print statements
pytest -s
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files `test_*.py`
- Name test functions `test_*`
- Use descriptive test names
- Aim for >90% code coverage

Example test:

```python
def test_resource_creation(sample_resource: Resource) -> None:
    """Test creating a valid resource."""
    assert sample_resource.title == "Test Resource"
    assert sample_resource.is_free is True
    assert sample_resource.rating == 4.5
```

## 📤 Submitting Changes

### 1. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 2. Create a Pull Request

1. Go to the original repository on GitHub
2. Click "New Pull Request"
3. Select your fork and branch
4. Fill in the PR template with:
   - Description of changes
   - Related issues
   - Screenshots (if applicable)
   - Checklist completion

### 3. PR Review Process

- Automated checks will run (CI/CD)
- A maintainer will review your code
- Address any feedback
- Once approved, your PR will be merged!

## 📚 Adding New Resources

### To Add a Resource to the README

1. Find the appropriate section
2. Add your resource following the existing format
3. Ensure all links work
4. Add relevant badges/icons

### To Add a Resource to the CLI Tool

1. Edit `src/faang_interview/resources.py`
2. Add a new `Resource` instance to the `RESOURCES` list:

```python
Resource(
    title="Your Resource",
    description="A brief description",
    url="https://example.com",
    resource_type=ResourceType.COURSE,  # BOOK, VIDEO, PLATFORM, etc.
    category=ResourceCategory.CODING,   # SYSTEM_DESIGN, AI_ML, etc.
    difficulty=DifficultyLevel.INTERMEDIATE,  # BEGINNER, ADVANCED, EXPERT
    is_free=True,
    price="$99",  # if not free
    rating=4.8,
    tags=["python", "algorithms"],
),
```

3. Run tests to ensure everything works:

```bash
hatch run test
```

## 🐛 Reporting Bugs

### Before Submitting a Bug Report

- Check existing issues
- Verify you're using the latest version
- Collect information about your environment

### Submitting a Bug Report

Create an issue with:

- Clear, descriptive title
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details (OS, Python version, etc.)
- Screenshots (if applicable)

## 💡 Feature Requests

We welcome feature requests! Please:

1. Check if the feature already exists or is planned
2. Clearly describe the feature and its benefits
3. Provide examples of how it would be used

## 📖 Documentation

### Updating Documentation

- Keep documentation up-to-date with code changes
- Use clear, concise language
- Add examples where helpful
- Follow existing documentation style

### Building Documentation Locally

```bash
# Build docs
hatch run docs:build

# Serve docs locally
hatch run docs:serve
```

## 🎯 Development Scripts

```bash
# Format code
hatch run format

# Lint code
hatch run lint

# Type check
hatch run type-check

# Run tests
hatch run test

# Run tests with coverage
hatch run test-cov

# Run all checks (format, lint, type-check, test)
hatch run all
```

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## ❓ Questions?

- Open an issue for questions
- Check existing issues and discussions
- Be patient and respectful

---

Thank you for contributing to Awesome FAANG Interview Resources! 🚀

**Happy Coding!** 💻✨
