from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()

input_file_path = BASE_DIR / "input.txt"

EDGE = (0, 136)
CORNER = ((0, 136), (136, 0), (0, 0), (136, 136))


def accessible_rule(neighbors: list[str]) -> bool:
    """
    A roll is accessible if fewer than four adjacent positions
    contain another roll '@'.
    """
    return neighbors.count("@") < 4


def check_interior(rolls: list[list[str]], pos: tuple, rule_fn) -> bool:
    """
    Interior cell: 8 neighbors exist.
    rule_fn(neighbors) -> bool decides validity.
    """
    r, c = pos
    neighbors = [
        rolls[r - 1][c - 1],
        rolls[r - 1][c],
        rolls[r - 1][c + 1],
        rolls[r][c - 1],
        rolls[r][c + 1],
        rolls[r + 1][c - 1],
        rolls[r + 1][c],
        rolls[r + 1][c + 1],
    ]
    return rule_fn(neighbors)


def check_edge(rolls: list[list[str]], pos: tuple, rule_fn) -> bool:
    """
    Edge cell: has fewer than 8 neighbors.
    Collects only valid neighbor positions.
    """
    r, c = pos
    rows, cols = len(rolls), len(rolls[0])
    neighbors = []

    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbors.append(rolls[nr][nc])

    return rule_fn(neighbors)


def check_corner(rolls: list[list[str]], pos: tuple, rule_fn) -> bool:
    """
    Corner cell: at most 3 neighbors.
    (Same bounded neighbor logic as edge.)
    """
    r, c = pos
    rows, cols = len(rolls), len(rolls[0])
    neighbors = []

    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbors.append(rolls[nr][nc])

    return rule_fn(neighbors)


def is_accessible(rolls: list[list[str]], pos: tuple, *arg) -> bool:
    answer = False
    global EDGE, CORNER
    if pos in CORNER:
        answer = check_corner(rolls, pos, accessible_rule)
    elif pos[0] in EDGE or pos[1] in EDGE:
        answer = check_edge(rolls, pos, accessible_rule)
    else:
        answer = check_interior(rolls, pos, accessible_rule)

    return answer


def get_x(rolls: list[list[str]], rows: int, cols: int, *arg):
    ans = 0
    for i in range(0, rows):
        for j in range(0, cols):
            pos = (i, j)
            if rolls[i][j] == "@" and is_accessible(rolls, pos):
                ans += 1
                rolls[i][j] = "x"

    return ans


def main(*arg):
    with open(input_file_path, "r") as file:
        data = file.read()
    data = data.split("\n")
    rolls = list(map(list, data))
    global CORNER
    global EDGE
    rows, cols = len(rolls), len(rolls[0])
    end = rows - 1
    EDGE = (0, end)
    CORNER = ((0, end), (end, 0), (0, 0), (end, end))

    temp = True
    answer = 0
    while temp:
        temp = get_x(rolls, rows, cols)
        answer += temp

    print(answer)


if __name__ == "__main__":
    main()


BASE_DIR = Path(__file__).parent.resolve()
input_file_path = BASE_DIR / "input.txt"


def accessible(neighbors):
    return neighbors.count("@") < 4


def neighbors_of(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dr, dc in offsets:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield grid[nr][nc]


def perform_pass(grid):
    """
    Return number of '@' cells that become 'x' this round.
    Does not mutate while scanning.
    """
    rows, cols = len(grid), len(grid[0])
    to_flip = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                neigh = list(neighbors_of(grid, r, c))
                if accessible(neigh):
                    to_flip.append((r, c))

    for r, c in to_flip:
        grid[r][c] = "x"

    return len(to_flip)


def main():
    data = Path(input_file_path).read_text().splitlines()
    grid = list(map(list, data))

    total = 0
    while True:
        changed = perform_pass(grid)
        if not changed:
            break
        total += changed

    print(total)


if __name__ == "__main__":
    main()
