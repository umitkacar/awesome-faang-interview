.PHONY: help install dev test lint format type-check clean build publish

.DEFAULT_GOAL := help

help: ## 📖 Show this help message
	@echo "🚀 Awesome FAANG Interview Resources - Development Commands"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## 📦 Install package in development mode
	pip install -e ".[dev]"

install-hatch: ## 🎩 Install Hatch
	pip install hatch

dev: install ## 🛠️ Set up development environment
	pre-commit install
	@echo "✅ Development environment ready!"

test: ## 🧪 Run tests
	hatch run test

test-cov: ## 📊 Run tests with coverage
	hatch run test-cov

test-watch: ## 👀 Run tests in watch mode
	hatch run pytest-watch

lint: ## 🔍 Run linter (Ruff)
	hatch run lint

lint-fix: ## 🔧 Run linter with auto-fix
	hatch run ruff check src tests --fix

format: ## 🎨 Format code (Black + Ruff)
	hatch run format

format-check: ## ✅ Check code formatting
	hatch run format-check

type-check: ## 🔎 Run type checker (MyPy)
	hatch run type-check

all: format lint type-check test-cov ## ✨ Run all checks (format, lint, type-check, test)
	@echo "✅ All checks passed!"

pre-commit: ## 🎣 Run pre-commit hooks
	pre-commit run --all-files

pre-commit-update: ## 🔄 Update pre-commit hooks
	pre-commit autoupdate

clean: ## 🧹 Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .eggs/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf coverage.xml
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean ## 🏗️ Build package
	hatch build

publish-test: build ## 📤 Publish to TestPyPI
	hatch publish -r test

publish: build ## 🚀 Publish to PyPI
	hatch publish

# CLI Commands
cli-list: ## 📚 List all resources
	hatch run faang list

cli-stats: ## 📊 Show resource statistics
	hatch run faang stats

cli-roadmap: ## 🗺️ Show learning roadmap
	hatch run faang roadmap

cli-categories: ## 📂 Show resource categories
	hatch run faang categories

# Documentation
docs-build: ## 📚 Build documentation
	hatch run docs:build

docs-serve: ## 🌐 Serve documentation locally
	hatch run docs:serve

# Git helpers
git-setup: ## 🔧 Set up git hooks
	pre-commit install
	git config --local commit.template .gitmessage

git-clean: ## 🧹 Clean git branches
	git fetch --prune
	git branch --merged | grep -v "\*" | xargs -n 1 git branch -d

# Security
security: ## 🔒 Run security checks
	bandit -r src -c pyproject.toml
	safety check

# Performance
profile: ## ⚡ Profile code performance
	python -m cProfile -o profile.stats src/faang_interview/cli.py
	python -c "import pstats; p = pstats.Stats('profile.stats'); p.sort_stats('cumulative').print_stats(20)"

# Dependencies
deps-update: ## 🔄 Update dependencies
	pip install --upgrade pip hatch
	pre-commit autoupdate

deps-list: ## 📋 List installed dependencies
	pip list

deps-tree: ## 🌲 Show dependency tree
	pip install pipdeptree
	pipdeptree

# Docker (if needed in future)
docker-build: ## 🐳 Build Docker image
	docker build -t awesome-faang-interview .

docker-run: ## 🏃 Run Docker container
	docker run -it awesome-faang-interview

# Info
info: ## ℹ️ Show project information
	@echo "📦 Package: awesome-faang-interview"
	@echo "🐍 Python: $(shell python --version)"
	@echo "📍 Location: $(shell pwd)"
	@echo "🔀 Git Branch: $(shell git branch --show-current)"
	@echo "📝 Git Status: $(shell git status --short)"
