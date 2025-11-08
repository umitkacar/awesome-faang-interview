# 🛠️ Development Guide

This guide covers the development setup and workflow for the Awesome FAANG Interview Resources project.

## 📦 Tech Stack

### Build System
- **[Hatch](https://hatch.pypa.io/)** - Modern, standards-based Python project manager
  - Build backend & dependency management
  - Environment management
  - Script runners

### Code Quality Tools
- **[Ruff](https://github.com/astral-sh/ruff)** - Ultra-fast Python linter & formatter
  - Replaces Flake8, isort, pyupgrade, and more
  - 10-100x faster than existing tools
  - Auto-fixes many issues

- **[Black](https://github.com/psf/black)** - The uncompromising code formatter
  - Line length: 100
  - Ensures consistent code style

- **[MyPy](https://mypy-lang.org/)** - Static type checker
  - Strict mode enabled
  - Catches type errors before runtime

### Testing
- **[Pytest](https://pytest.org/)** - Testing framework
  - Simple and scalable
  - Rich plugin ecosystem

- **[Coverage.py](https://coverage.readthedocs.io/)** - Code coverage measurement
  - Track test coverage
  - Generate HTML reports

### Pre-commit Hooks
- **[pre-commit](https://pre-commit.com/)** - Git hooks framework
  - Runs checks before every commit
  - Ensures code quality automatically

## 🚀 Quick Start

### 1. Install Hatch

```bash
# Using pip
pip install hatch

# Or using pipx (recommended)
pipx install hatch
```

### 2. Clone the Repository

```bash
git clone https://github.com/umitkacar/awesome-faang-interview.git
cd awesome-faang-interview
```

### 3. Install Pre-commit Hooks

```bash
pre-commit install
```

That's it! Hatch will automatically create and manage environments for you.

## 🎯 Development Commands

### Using Hatch (Recommended)

```bash
# Run tests
hatch run test

# Run tests with coverage
hatch run test-cov

# Lint code
hatch run lint

# Format code
hatch run format

# Type check
hatch run type-check

# Run all checks
hatch run all
```

### Using Make

```bash
# Show all available commands
make help

# Run tests
make test

# Run all checks
make all

# Clean build artifacts
make clean

# Build package
make build
```

## 📁 Project Structure

```
awesome-faang-interview/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD
├── src/
│   └── faang_interview/
│       ├── __init__.py         # Package initialization
│       ├── cli.py              # CLI application (Typer)
│       ├── core.py             # Core data models (Pydantic)
│       └── resources.py        # Resource database
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Pytest fixtures
│   ├── test_core.py            # Tests for core models
│   └── test_resources.py      # Tests for resources
├── .pre-commit-config.yaml     # Pre-commit hooks configuration
├── pyproject.toml              # Project configuration (PEP 518)
├── Makefile                    # Development commands
├── README.md                   # Project README
├── CONTRIBUTING.md             # Contribution guidelines
└── DEVELOPMENT.md              # This file
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

# Run with print statements
pytest -s

# Run and show local variables on failure
pytest -l

# Run failed tests from last run
pytest --lf

# Run tests matching a pattern
pytest -k "test_resource"
```

### Coverage Reports

```bash
# Generate coverage report
hatch run test-cov

# View HTML coverage report
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

## 🎨 Code Quality

### Formatting

```bash
# Format all code
hatch run format

# Check formatting without changes
hatch run format-check

# Format specific file
black src/faang_interview/core.py
```

### Linting

```bash
# Lint all code
hatch run lint

# Lint with auto-fix
ruff check src tests --fix

# Lint specific file
ruff check src/faang_interview/cli.py

# Show all violations (including fixed)
ruff check src tests --show-fixes
```

### Type Checking

```bash
# Type check all code
hatch run type-check

# Type check specific file
mypy src/faang_interview/core.py

# Generate type checking report
mypy src --html-report mypy-report
```

## 🎣 Pre-commit Hooks

### Running Hooks

```bash
# Run on all files
pre-commit run --all-files

# Run specific hook
pre-commit run ruff --all-files

# Update hooks to latest version
pre-commit autoupdate

# Skip hooks for a commit (not recommended)
git commit --no-verify
```

### Installed Hooks

- ✅ File checks (large files, merge conflicts, etc.)
- ✅ Ruff (linting & auto-fixes)
- ✅ Black (code formatting)
- ✅ MyPy (type checking)
- ✅ PyUpgrade (syntax upgrades)
- ✅ Prettier (YAML, Markdown, JSON)
- ✅ Markdownlint (Markdown linting)
- ✅ ShellCheck (shell script linting)
- ✅ Bandit (security linting)
- ✅ Codespell (spell checking)

## 🏗️ Building

### Build Package

```bash
# Build using Hatch
hatch build

# Build using Make
make build

# Output: dist/awesome_faang_interview-1.0.0.tar.gz
#         dist/awesome_faang_interview-1.0.0-py3-none-any.whl
```

## 🔧 Configuration Files

### pyproject.toml

Central configuration for:
- Project metadata
- Dependencies
- Build system (Hatch)
- Tool configurations (Ruff, Black, MyPy, Pytest, Coverage)

### .pre-commit-config.yaml

Defines all pre-commit hooks and their configurations.

## 🐛 Debugging

### Using pdb

```python
import pdb; pdb.set_trace()
```

### Using pytest with pdb

```bash
# Drop into pdb on failure
pytest --pdb

# Drop into pdb on first failure
pytest -x --pdb
```

### Profiling

```bash
# Profile code
python -m cProfile -o profile.stats src/faang_interview/cli.py

# View profile results
python -c "import pstats; p = pstats.Stats('profile.stats'); p.sort_stats('cumulative').print_stats(20)"

# Or use make
make profile
```

## 📊 CI/CD

### GitHub Actions

Our CI/CD pipeline runs on every push and PR:

1. **Lint** - Ruff & Black checks on multiple Python versions
2. **Type Check** - MyPy type checking
3. **Test** - Pytest on multiple OS and Python versions
4. **Security** - Bandit & Safety checks
5. **Build** - Package build verification
6. **Pre-commit** - All pre-commit hooks

View workflow: `.github/workflows/ci.yml`

### Local CI Simulation

```bash
# Run all checks like CI does
make all

# Or using Hatch
hatch run all
```

## 🔐 Security

### Security Scanning

```bash
# Run Bandit (security linter)
bandit -r src -c pyproject.toml

# Check dependencies for vulnerabilities
safety check

# Or use make
make security
```

## 📦 Dependencies

### Managing Dependencies

```bash
# Update dependencies
pip install --upgrade pip hatch

# Update pre-commit hooks
pre-commit autoupdate

# Or use make
make deps-update
```

### Viewing Dependencies

```bash
# List installed packages
pip list

# Show dependency tree
pip install pipdeptree
pipdeptree

# Or use make
make deps-list
make deps-tree
```

## 🌍 Environment Management

Hatch automatically manages environments for you, but you can also:

```bash
# Create environment
hatch env create

# Show environment info
hatch env show

# Remove environment
hatch env remove default

# Run command in environment
hatch run python --version
```

## 💡 Tips & Best Practices

### 1. Run Tests Before Committing

```bash
make test
# or
hatch run test
```

### 2. Use Pre-commit Hooks

They catch issues before CI does!

### 3. Write Type Hints

MyPy is configured in strict mode. Always add type hints:

```python
def calculate_sum(a: int, b: int) -> int:
    return a + b
```

### 4. Maintain High Coverage

Aim for >90% code coverage. Check with:

```bash
hatch run test-cov
```

### 5. Follow Commit Conventions

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add new resource filter
fix: correct rating validation
docs: update installation guide
```

## 🆘 Troubleshooting

### Virtual Environment Issues

```bash
# Remove and recreate Hatch environments
hatch env prune
hatch env create
```

### Pre-commit Hook Failures

```bash
# Update hooks
pre-commit autoupdate

# Clear cache
pre-commit clean
pre-commit install
```

### Import Errors

```bash
# Reinstall in editable mode
pip install -e ".[dev]"
```

### Test Failures

```bash
# Run with verbose output
pytest -vv

# Show local variables on failure
pytest -l

# Run with print statements
pytest -s
```

## 📚 Additional Resources

- [Hatch Documentation](https://hatch.pypa.io/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Black Documentation](https://black.readthedocs.io/)
- [MyPy Documentation](https://mypy.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Pre-commit Documentation](https://pre-commit.com/)

---

Happy Hacking! 🚀✨
