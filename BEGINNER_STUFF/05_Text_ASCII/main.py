import random
from datetime import datetime
from pathlib import Path

from art import (
    DECORATION_NAMES,
    FONT_NAMES,
    decor_list,
    font_list,
    text2art,
    tprint,
)


def generate_random_art(text):
    if not font_list:
        raise ValueError("No fonts available in font_list.")
    if not decor_list:
        raise ValueError("No decorations available in decor_list.")

    tprint("test", font="random")
    font = random.choice(FONT_NAMES)
    decor = random.choice(DECORATION_NAMES)

    art_output = text2art(text, font=font)
    decorated = (
        f"{decor * 10}\n{art_output}{decor * 10}\n\nFont: {font} | Decor: {decor}"
    )
    return decorated


def show_intro():
    tprint("ASCII  Party", font="block")
    print("🎉 Welcome to the Ultimate ASCII Terminal Party 🎉")
    print(
        f"Vibe with {len(FONT_NAMES)} fonts and {len(DECORATION_NAMES)} decorations!\n"
    )


def save_to_file(path, content, filename="ascii_dump.txt"):
    with open(path / filename, "a", encoding="utf-8") as f:
        f.write(f"\n\n[{datetime.now()}]\n")
        f.write(content)
        f.write("\n" + "=" * 80 + "\n")


def generate_sequential_filename(directory, base_name="ascii_dump", ext=".txt"):
    count = 1
    while True:
        filename = f"{base_name}_{count:03}{ext}"
        full_path = directory / filename
        if not full_path.exists():
            return full_path
        count += 1


def main(cur_dir):
    save_path = cur_dir / "ascii_art_res"
    save_path.mkdir(exist_ok=True)  # create the folder if it doesn't exist
    show_intro()

    while True:
        try:
            text = input("📝 Enter text (or type 'exit' to quit): ").strip()
            if text.lower() == "exit":
                tprint("Goodbye!", font="cybermedium")
                break

            result = generate_random_art(text)
            print(result)

            # Generate a new file with an incremental name
            file_path = generate_sequential_filename(save_path)
            save_to_file(file_path.parent, result, file_path.name)

            print(f"✅ Saved to {file_path.name}\n")

        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    cur_dir = Path(__file__).resolve().parent
    main(cur_dir)
