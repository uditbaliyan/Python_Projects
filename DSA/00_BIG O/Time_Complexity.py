import matplotlib
import matplotlib.pyplot as plt
import pathlib
import math
import numpy as np

matplotlib.use("Agg")

# Directory for saving images
IMG_DIR = pathlib.Path("Time_Complexity_IMG")
IMG_DIR.mkdir(exist_ok=True)

# Input range (smaller for fast-growing functions)
inputs = np.arange(1, 50, 1)


# ---- Define time complexity functions ----
def O_logN(n):
    return np.log2(n)


def O_N(n):
    return n


def O_N2(n):
    return n**2


def O_N3(n):
    return n**3


def O_2N(n):
    return 2**n


def O_Nfact(n):
    return [math.factorial(int(i)) for i in n]


# ---- Store all complexities ----
complexities = {
    "O(log N)": O_logN(inputs),
    "O(N)": O_N(inputs),
    "O(N²)": O_N2(inputs),
    "O(N³)": O_N3(inputs),
    "O(2ⁿ)": O_2N(inputs),
    "O(N!)": O_Nfact(inputs),
}

# ---- Generate individual plots ----
for label, values in complexities.items():
    plt.figure(figsize=(6, 4))
    plt.plot(inputs, values, linewidth=2)
    plt.xlabel("Input Size (N)")
    plt.ylabel("Operations")
    plt.title(f"Time Complexity: {label}")
    plt.grid(True)
    plt.tight_layout()
    safe_label = (
        label.replace("/", "_")
        .replace("²", "2")
        .replace("³", "3")
        .replace("!", "fact")
        .replace("ⁿ", "n")
    )
    plt.savefig(IMG_DIR / f"Big_O_{safe_label}.png", dpi=300)
    plt.close()

# ---- Combined Comparison Plot ----
plt.figure(figsize=(10, 6))
for label, values in complexities.items():
    # Restrict range for large growth
    limit = 15 if ("!" in label or "2ⁿ" in label) else len(inputs)
    plt.plot(inputs[:limit], values[:limit], label=label, linewidth=2)
plt.xlabel("Input Size (N)")
plt.ylabel("Operations (relative growth)")
plt.title("Comparison of Time Complexities")
plt.legend()
plt.yscale("log")  # Helps visualize big differences
plt.grid(True, which="both")
plt.tight_layout()
plt.savefig(IMG_DIR / "Big_O_Comparison.png", dpi=300)
plt.close()

# ---- Theoretical Table Data ----
notations = [
    "O(1)",
    "O(log N)",
    "O(N)",
    "O(N log N)",
    "O(N²)",
    "O(N³)",
    "O(2ⁿ)",
    "O(N!)",
]
names = [
    "Constant Time",
    "Logarithmic Time",
    "Linear Time",
    "Linearithmic Time",
    "Quadratic Time",
    "Cubic Time",
    "Exponential Time",
    "Factorial Time",
]
examples = [
    "Accessing array element",
    "Binary search",
    "Linear search",
    "Merge sort, Heap sort",
    "Bubble sort, Insertion sort",
    "Matrix multiplication (naïve)",
    "Recursive subset generation",
    "Travelling Salesman (brute-force)",
]
growth = [
    "Fastest (best)",
    "Very efficient",
    "Moderate",
    "Acceptable for large N",
    "Slow (only small N feasible)",
    "Very slow",
    "Explosive growth",
    "Impractical (huge N)",
]

# ---- Print Table to Console ----
print("\n===== Time Complexity Comparison Table =====\n")
header = (
    f"{"Notation":<10} | {"Name":<20} | {"Example Algorithm":<35} | {"Growth Nature"}"
)
print(header)
print("-" * len(header))
for i in range(len(notations)):
    print(f"{notations[i]:<10} | {names[i]:<20} | {examples[i]:<35} | {growth[i]}")

# ---- Save Table as an Image ----
fig, ax = plt.subplots(figsize=(10, 3))
ax.axis("off")

table_data = []
for i in range(len(notations)):
    table_data.append([notations[i], names[i], examples[i], growth[i]])

columns = ["Notation", "Name", "Example Algorithm", "Growth Nature"]
table = ax.table(cellText=table_data, colLabels=columns, loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.2, 1.2)

plt.tight_layout()
plt.savefig(IMG_DIR / "Big_O_Theory_Table.png", dpi=300)
plt.close()

print("\n✅ All plots and tables saved in:", IMG_DIR.resolve())

# Big O(N)

# Big O(N^2)
# Big O(N^3)
# Big O(2^N)
# Big O(N!)


# Big O()
# Big O()
# Big O()
# Big O()
# Big O()
