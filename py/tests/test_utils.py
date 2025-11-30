from utils import read_data_file


def tests_work():
    """Tests the basic happy path."""
    assert 4 + 5 == 9


def test_file_read():
    assert read_data_file("test.txt", " ") == ["hello", "world"]
