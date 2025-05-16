
from pathlib import Path


def grab_list_of_problems(file_path: Path) -> list[str]:
    '''
    Grab the list of problems from the provided file.

    Args:
        file_path (Path): The file to grab the list from.

    Returns:
        list[str]: The list of problems.

    Notes:
        - Returns an empty list if the file does not exist.
        - Returns each problem without newlines attached.
    '''
    # Check if the file exists
    if not file_path.exists():
        return []

    # Open the file, and return the contents without newlines
    problems = []
    with file_path.open('r', encoding='utf-8') as file:
        for problem in file.readlines():
            problems.append(problem.strip())

    return problems
