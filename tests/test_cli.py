"""Tests for CLI commands."""

from typer.testing import CliRunner

from faang_interview.cli import app

runner = CliRunner()


class TestCLICommands:
    """Tests for CLI commands."""

    def test_help_command(self) -> None:
        """Test help command."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "FAANG Interview Resources CLI" in result.stdout

    def test_list_command(self) -> None:
        """Test list command."""
        result = runner.invoke(app, ["list"])
        assert result.exit_code == 0
        assert "FAANG Interview Resources" in result.stdout

    def test_stats_command(self) -> None:
        """Test stats command."""
        result = runner.invoke(app, ["stats"])
        assert result.exit_code == 0
        assert "Resource Statistics" in result.stdout
        assert "Total Resources:" in result.stdout

    def test_categories_command(self) -> None:
        """Test categories command."""
        result = runner.invoke(app, ["categories"])
        assert result.exit_code == 0
        assert "Resource Categories" in result.stdout

    def test_roadmap_command(self) -> None:
        """Test roadmap command."""
        result = runner.invoke(app, ["roadmap"])
        assert result.exit_code == 0
        assert "FAANG Interview Preparation Roadmap" in result.stdout
        assert "Week" in result.stdout

    def test_search_command(self) -> None:
        """Test search command."""
        result = runner.invoke(app, ["search", "leetcode"])
        assert result.exit_code == 0

    def test_list_with_free_filter(self) -> None:
        """Test list command with --free filter."""
        result = runner.invoke(app, ["list", "--free"])
        assert result.exit_code == 0

    def test_version_command(self) -> None:
        """Test version command."""
        result = runner.invoke(app, ["--version"])
        assert result.exit_code == 0
        assert "version" in result.stdout.lower()
