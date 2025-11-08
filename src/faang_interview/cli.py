"""Command-line interface for FAANG interview resources."""

from typing import Optional

import typer
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.tree import Tree

from faang_interview import __version__
from faang_interview.core import Resource, ResourceCategory, ResourceType
from faang_interview.resources import get_all_resources, get_resources_by_category

app = typer.Typer(
    name="faang",
    help="🚀 Awesome FAANG Interview Resources CLI",
    add_completion=True,
)

console = Console()


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        rprint(f"[bold blue]FAANG Interview CLI[/bold blue] version: [green]{__version__}[/green]")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit.",
    ),
) -> None:
    """Awesome FAANG Interview Resources - CLI Tool."""


@app.command(name="list")
def list_resources(
    category: Optional[ResourceCategory] = typer.Option(
        None, "--category", "-c", help="Filter by category"
    ),
    resource_type: Optional[ResourceType] = typer.Option(
        None, "--type", "-t", help="Filter by type"
    ),
    free_only: bool = typer.Option(False, "--free", "-f", help="Show only free resources"),
) -> None:
    """📚 List all available resources."""
    resources = get_all_resources()

    # Apply filters
    if category:
        resources = [r for r in resources if r.category == category]
    if resource_type:
        resources = [r for r in resources if r.resource_type == resource_type]
    if free_only:
        resources = [r for r in resources if r.is_free]

    if not resources:
        rprint("[yellow]No resources found matching the criteria.[/yellow]")
        return

    table = Table(
        title="🚀 FAANG Interview Resources", show_header=True, header_style="bold magenta"
    )
    table.add_column("Title", style="cyan", no_wrap=False)
    table.add_column("Type", style="green")
    table.add_column("Category", style="blue")
    table.add_column("Free", style="yellow", justify="center")
    table.add_column("Rating", style="red", justify="center")

    for resource in resources:
        free_icon = "✅" if resource.is_free else "💰"
        rating_str = f"{resource.rating:.1f}⭐" if resource.rating else "N/A"

        table.add_row(
            resource.title,
            resource.resource_type.value,
            resource.category.value,
            free_icon,
            rating_str,
        )

    console.print(table)
    rprint(f"\n[bold green]Total: {len(resources)} resources[/bold green]")


@app.command()
def categories() -> None:
    """📂 Show all resource categories."""
    tree = Tree("🎯 [bold]Resource Categories[/bold]")

    for category in ResourceCategory:
        resources = get_resources_by_category(category)
        branch = tree.add(f"[cyan]{category.value}[/cyan] ({len(resources)} resources)")

        # Group by type
        by_type: dict[ResourceType, list[Resource]] = {}
        for resource in resources:
            if resource.resource_type not in by_type:
                by_type[resource.resource_type] = []
            by_type[resource.resource_type].append(resource)

        for res_type, res_list in by_type.items():
            branch.add(f"[green]{res_type.value}[/green]: {len(res_list)}")

    console.print(tree)


@app.command()
def roadmap() -> None:
    """🗺️ Show learning roadmap."""
    roadmap_text = """
    [bold cyan]16-Week FAANG Interview Preparation Roadmap[/bold cyan]

    [bold yellow]Week 1-2:[/bold yellow] DSA Basics
    • NeetCode Roadmap
    • VisuAlgo
    • Big O Cheat Sheet

    [bold yellow]Week 3-6:[/bold yellow] Problem Solving
    • LeetCode Grind 75 (Easy → Medium)
    • Focus on patterns

    [bold yellow]Week 7-10:[/bold yellow] Advanced Problems
    • Blind 75
    • NeetCode 150
    • Hard problems

    [bold yellow]Week 11-12:[/bold yellow] System Design
    • ByteByteGo
    • System Design Primer
    • Design patterns

    [bold yellow]Week 13-14:[/bold yellow] Mock Interviews
    • Pramp
    • Interviewing.io
    • Practice with peers

    [bold yellow]Week 15-16:[/bold yellow] Final Prep
    • Behavioral questions
    • Company-specific prep
    • Resume polish

    [bold green]🎯 Recommended: 4-5 hours/day consistently![/bold green]
    """

    panel = Panel(roadmap_text, title="🚀 FAANG Roadmap", border_style="blue")
    console.print(panel)


@app.command()
def stats() -> None:
    """📊 Show resource statistics."""
    resources = get_all_resources()

    total = len(resources)
    free_count = sum(1 for r in resources if r.is_free)
    paid_count = total - free_count

    # Count by category
    by_category: dict[ResourceCategory, int] = {}
    for resource in resources:
        by_category[resource.category] = by_category.get(resource.category, 0) + 1

    # Count by type
    by_type: dict[ResourceType, int] = {}
    for resource in resources:
        by_type[resource.resource_type] = by_type.get(resource.resource_type, 0) + 1

    stats_text = f"""
    [bold cyan]📊 Resource Statistics[/bold cyan]

    [bold]Total Resources:[/bold] {total}
    [bold green]Free:[/bold green] {free_count} ({free_count/total*100:.1f}%)
    [bold yellow]Paid:[/bold yellow] {paid_count} ({paid_count/total*100:.1f}%)

    [bold cyan]By Category:[/bold cyan]
    """

    for category, count in sorted(by_category.items(), key=lambda x: x[1], reverse=True):
        stats_text += f"\n    • {category.value}: {count}"

    stats_text += "\n\n[bold cyan]By Type:[/bold cyan]"
    for res_type, count in sorted(by_type.items(), key=lambda x: x[1], reverse=True):
        stats_text += f"\n    • {res_type.value}: {count}"

    panel = Panel(stats_text, title="📈 Statistics", border_style="green")
    console.print(panel)


@app.command()
def search(
    query: str = typer.Argument(..., help="Search query"),
) -> None:
    """🔍 Search for resources."""
    resources = get_all_resources()
    query_lower = query.lower()

    results = [
        r
        for r in resources
        if query_lower in r.title.lower()
        or query_lower in r.description.lower()
        or any(query_lower in tag.lower() for tag in r.tags)
    ]

    if not results:
        rprint(f"[yellow]No resources found for query: '{query}'[/yellow]")
        return

    table = Table(
        title=f"🔍 Search Results for '{query}'", show_header=True, header_style="bold magenta"
    )
    table.add_column("Title", style="cyan", no_wrap=False)
    table.add_column("Description", style="white", no_wrap=False)
    table.add_column("Category", style="blue")
    table.add_column("Type", style="green")

    for resource in results:
        table.add_row(
            resource.title,
            (
                resource.description[:50] + "..."
                if len(resource.description) > 50
                else resource.description
            ),
            resource.category.value,
            resource.resource_type.value,
        )

    console.print(table)
    rprint(f"\n[bold green]Found: {len(results)} resources[/bold green]")


if __name__ == "__main__":
    app()
