import pathlib


def get_path():
    # Get the current working directory
    current_dir = pathlib.Path(__file__).parent.resolve()

    # Construct the path to the 'OOPs' directory
    oops_path = current_dir.parent

    # Return the absolute path as a string
    return str(oops_path)


def main():
    # Print the path to the 'OOPs' directory
    print(get_path())
    print("Path to OOPs directory:", get_path())


if __name__ == "__main__":
    main()
