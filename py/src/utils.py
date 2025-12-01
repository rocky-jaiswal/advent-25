from pathlib import Path


def read_data_file(filename: str, delimiter: str = "\n") -> list[str]:
    """Read a file from the data folder and return split contents."""
    data_dir = Path(__file__).parent.parent / "data"
    file_path = data_dir / filename

    content = ""

    with open(file_path, "r") as f:
        content = f.read()

    return content.split(delimiter)
