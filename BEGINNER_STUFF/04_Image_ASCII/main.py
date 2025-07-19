from pathlib import Path

from ascii_magic import AsciiArt


def main(path, *args):
    """Docstring"""
    image_dir = path / "Images/image_1.png"
    # res = path / "res/ascii_art.html"
    b = path / "res/ascii_art.txt"
    my_art = AsciiArt.from_image(image_dir)
    # my_art.to_terminal(columns=200, back=Back.BLUE)
    # my_art.to_html_file(res, columns=200, width_ratio=2)
    my_art.to_file(b, columns=100, width_ratio=2, monochrome=True)


def compare(a, b):
    if a is b:
        print("same object")
    if a == b:
        print("same value")
    if type(a) is type(b):
        print("same type")


if __name__ == "__main__":
    cur_dir = Path(__file__).resolve().parent
    main(cur_dir)
    # a="aa"*100
    # b="aa"*100

    import sys

    a = sys.intern("aa" * 1000000000)
    b = sys.intern("aa" * 1000000000)
    # a = sys.intern("aa" * 1000000000) system crash
    # b = sys.intern("aa" * 1000000000)
    compare(a, b)

    # compare(a,b)
    # b=2
    # compare(a,b)
