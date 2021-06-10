from src import main
from src.utils import logger


def test_get_files_from_dir():
    result = main.get_files_from_dir("./")
    logger.info(result)


def test_file():
    name = "name"
    name_with_extension = "name.csv"
    path = "dir/name.csv"
    result = main.File(name, name_with_extension, path)

    assert result.name == name
    assert result.name_with_extension == name_with_extension
    assert result.path == path
