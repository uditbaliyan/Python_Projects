from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def categorize_dynamic(obj: object) -> dict[str, list[str]]:
    """Dynamically categorize methods of an object."""
    methods = dir(obj)

    categories: dict[str, list[str]] = {
        "Dunder Methods": [],
        "Check Methods": [],  # isalpha, isdigit, etc.
        "Transform Methods": [],  # upper, lower, capitalize, replace...
        "Search Methods": [],  # find, index, startswith, endswith...
        "Other Methods": [],
    }

    for m in methods:
        if m.startswith("__") and m.endswith("__"):
            categories["Dunder Methods"].append(m)
        elif m.startswith("is"):
            categories["Check Methods"].append(m)
        elif any(
            m.startswith(prefix)
            for prefix in (
                "upper",
                "lower",
                "capitalize",
                "title",
                "swapcase",
                "replace",
            )
        ):
            categories["Transform Methods"].append(m)
        elif any(
            m in search
            for search in ("find", "index", "startswith", "endswith", "count")
        ):
            categories["Search Methods"].append(m)
        else:
            categories["Other Methods"].append(m)

    return {k: v for k, v in categories.items() if v}  # remove empty ones


def print_methods(obj: object, name: str) -> None:
    cats = categorize_dynamic(obj)
    console.print(Panel.fit(f"🔹 {name} methods", style="bold blue"))
    for cat, items in cats.items():
        console.print(Text(cat, style="bold magenta"))
        console.print(items, style="yellow")
        console.print()


# Example
print_methods("", "String")
