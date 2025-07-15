from pathlib import Path

from ascii_magic import AsciiArt


def main(path, *args):
    """Docstring"""
    image_dir = path / "Images/image_1.png"
    res = path / "res/ascii_art.html"
    my_art = AsciiArt.from_image(image_dir)
    # my_art.to_terminal(columns=200, back=Back.BLUE)
    my_art.to_html_file(res, columns=200, width_ratio=2)


if __name__ == "__main__":
    cur_dir = Path(__file__).resolve().parent
    main(cur_dir)
