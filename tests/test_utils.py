import pytest
from code_tutor.utils.code_parser import parse_python_code
from code_tutor.utils.file_handler import read_file, write_file


def test_parse_python_code():
    code = """
def hello_world():
    print("Hello, World!")
    """
    parsed = parse_python_code(code)
    assert 'hello_world' in parsed.function_names
    assert len(parsed.imports) == 0


def test_read_file(tmp_path):
    file_content = "Test content"
    file_path = tmp_path / "test_file.txt"
    file_path.write_text(file_content)

    assert read_file(str(file_path)) == file_content


def test_write_file(tmp_path):
    file_content = "Test content"
    file_path = tmp_path / "test_file.txt"

    write_file(str(file_path), file_content)
    assert file_path.read_text() == file_content