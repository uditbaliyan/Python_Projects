# what is array ?
# using list

from __future__ import annotations

from typing import Any, Dict, List

from rich.console import Console
from rich.panel import Panel
from rich.pretty import Pretty
from rich.text import Text

console = Console()


# ------------------------------
# Categorization for LIST (Array)
# ------------------------------
def categorize_list_methods(obj: Any) -> Dict[str, List[str]]:
    """Categorize methods for Python list (array-like)."""
    methods: List[str] = dir(obj)

    dunder = [m for m in methods if m.startswith("__") and m.endswith("__")]
    normal = [m for m in methods if not (m.startswith("__") and m.endswith("__"))]
    print(dunder)
    categories: Dict[str, List[str]] = {
        "Construction & Initialization": ["__new__", "__init__", "__init_subclass__"],
        "Attribute Management": [
            "__getattribute__",
            "__setattr__",
            "__delattr__",
            "__dir__",
        ],
        "Representation": ["__repr__", "__str__", "__format__", "__doc__"],
        "Comparison & Equality": [
            "__eq__",
            "__ne__",
            "__lt__",
            "__le__",
            "__gt__",
            "__ge__",
            "__hash__",
        ],
        "Container Protocol": [
            "__len__",
            "__getitem__",
            "__setitem__",
            "__delitem__",
            "__contains__",
        ],
        "Iteration & Reversal": ["__iter__", "__reversed__"],
        "Arithmetic": ["__add__", "__iadd__", "__mul__", "__imul__", "__rmul__"],
        "Pickling & State": ["__reduce__", "__reduce_ex__", "__getstate__"],
        "Memory & Introspection": ["__sizeof__", "__subclasshook__", "__class__"],
        "Normal Methods (List Operations)": normal,
    }

    return {
        cat: [m for m in items if m in methods]
        for cat, items in categories.items()
        if [m for m in items if m in methods]
    }


# ------------------------------
# Pretty Printer
# ------------------------------
def print_methods(obj: Any, name: str, categorizer) -> None:
    """Pretty-print categorized methods of an object with colors using rich."""
    categories = categorizer(obj)

    console.print(
        Panel.fit(f"🔹 [bold cyan]{name} methods by category[/]", style="bold blue")
    )

    for cat, items in categories.items():
        style = "green" if "Normal" in cat else "yellow"
        console.print(Text(cat, style="bold magenta"))
        console.print(Pretty(items), style=style)
        console.print()


# ------------------------------
# MAIN
# ------------------------------
def main() -> None:
    """Run examples for list and str separately."""
    sample_list: list = []

    print_methods(sample_list, "List (Array)", categorize_list_methods)


if __name__ == "__main__":
    main()
