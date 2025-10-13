import matplotlib
import matplotlib.pyplot as plt
import pathlib
import numpy as np

matplotlib.use("Agg")

# Directory for saving images
IMG_DIR = pathlib.Path("Space_Complexity_IMG")
IMG_DIR.mkdir(exist_ok=True)

# Input range
inputs = np.arange(1, 50, 1)


# ---- Define space complexity functions ----
def O_1(n):
    return np.ones_like(n)  # Constant space


def O_logN(n):
    return np.log2(n)  # Logarithmic space


def O_N(n):
    return n  # Linear space


def O_N2(n):
    return n**2  # Quadratic space


def O_N3(n):
    return n**3  # Cubic space


def O_2N(n):
    return 2**n  # Exponential space


# ---- Store all complexities ----
complexities = {
    "O(1)": O_1(inputs),
    "O(log N)": O_logN(inputs),
    "O(N)": O_N(inputs),
    "O(N²)": O_N2(inputs),
    "O(N³)": O_N3(inputs),
    "O(2ⁿ)": O_2N(inputs),
}

# ---- Generate individual plots ----
for label, values in complexities.items():
    plt.figure(figsize=(6, 4))
    plt.plot(inputs, values, linewidth=2)
    plt.xlabel("Input Size (N)")
    plt.ylabel("Memory Usage (units)")
    plt.title(f"Space Complexity: {label}")
    plt.grid(True)
    plt.tight_layout()
    safe_label = (
        label.replace("/", "_").replace("²", "2").replace("³", "3").replace("ⁿ", "n")
    )
    plt.savefig(IMG_DIR / f"Space_O_{safe_label}.png", dpi=300)
    plt.close()

# ---- Combined Comparison Plot ----
plt.figure(figsize=(10, 6))
for label, values in complexities.items():
    limit = 15 if ("2ⁿ" in label) else len(inputs)
    plt.plot(inputs[:limit], values[:limit], label=label, linewidth=2)
plt.xlabel("Input Size (N)")
plt.ylabel("Memory Usage (relative growth)")
plt.title("Comparison of Space Complexities")
plt.legend()
plt.yscale("log")  # Log scale for visibility
plt.grid(True, which="both")
plt.tight_layout()
plt.savefig(IMG_DIR / "Space_O_Comparison.png", dpi=300)
plt.close()

# ---- Theoretical Table ----
notations = ["O(1)", "O(log N)", "O(N)", "O(N log N)", "O(N²)", "O(2ⁿ)"]
names = [
    "Constant Space",
    "Logarithmic Space",
    "Linear Space",
    "Linearithmic Space",
    "Quadratic Space",
    "Exponential Space",
]
examples = [
    "In-place algorithms (swap, sum, etc.)",
    "Recursive binary search",
    "Storing array/list elements",
    "Merge sort (extra array)",
    "Matrix operations / 2D arrays",
    "Recursive power set generation",
]
growth = [
    "Minimal memory usage",
    "Very efficient",
    "Scales linearly with input",
    "Moderate growth",
    "High memory requirement",
    "Explosive, impractical",
]

# ---- Print Table to Console ----
print("\n===== Space Complexity Comparison Table =====\n")
header = (
    f"{"Notation":<10} | {"Name":<20} | {"Example Algorithm":<40} | {"Memory Growth"}"
)
print(header)
print("-" * len(header))
for i in range(len(notations)):
    print(f"{notations[i]:<10} | {names[i]:<20} | {examples[i]:<40} | {growth[i]}")

# ---- Save Table as an Image ----
fig, ax = plt.subplots(figsize=(10, 3))
ax.axis("off")

table_data = []
for i in range(len(notations)):
    table_data.append([notations[i], names[i], examples[i], growth[i]])

columns = ["Notation", "Name", "Example Algorithm", "Memory Growth"]
table = ax.table(cellText=table_data, colLabels=columns, loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.2, 1.2)
plt.tight_layout()
plt.savefig(IMG_DIR / "Space_O_Theory_Table.png", dpi=300)
plt.close()

print("\n✅ All space complexity plots and table saved in:", IMG_DIR.resolve())
