
from os import getcwd
from pathlib import Path


ROOT_DIR = Path(getcwd())


def grab_list_of_problems(file_path: Path) -> list[str]:
    '''
    Grab the list of problems from the provided file.

    Args:
        file_path (Path): The file to grab the list from.

    Returns:
        list[str]: The list of problems. Returns an
        empty list if the file does not exist.
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


def grab_unsolved_problems(tag: str) -> list[str]:
    '''
    Grabs the list of problems to solve, and the problems that have
        been solved, and returns the problems left to solve.

    Args:
        tag (str): The target directory.

    Returns:
        list[str]: The list of problems that still need to be solved.
    '''
    target_dir = ROOT_DIR / tag

    problems_file = (target_dir / 'problems').with_suffix('.txt')
    problems = grab_list_of_problems(problems_file)

    completed_file = (target_dir / 'complete').with_suffix('.txt')
    completed_problems = grab_list_of_problems(completed_file)

    return return_unique_list(problems, completed_problems, tag)


def return_unique_list(list1: list[str],
                       list2: list[str],
                       tag: str
                       ) -> list[str]:
    '''
    Return a combined list of the two provided, with only the unique elements.

    Args:
        list1 (list[str]): The first list of problems.
        list2 (list[str]): The second list of problems.
        tag (str): Whether it is 'rosetta' or 'simple', to determine sorting.
    '''
    # Grab the list of unique elements
    unique_list = list(set(list1) - set(list2))

    # If for rosetta, sort the list and return it as is
    if tag == 'rosetta_code':
        return sorted(unique_list)

    # For simple programming problems, each list of problems has the
    #   format `1. [problem]...`, and thus needs to be sorted by the
    #   number of problem instead of the first letter.
    # However, `.sort` returns `None`, so this cannot be one line.
    unique_list.sort(key=lambda x: int(x.split('. ')[0]))
    return unique_list


# Grab the problems from Rosetta that need to be solved
rosetta_problems = grab_unsolved_problems('rosetta_code')

# Grab the problems from Simple Programming Problems that need to be solved ===
simple_categories = [
    'elementary',
    'lists_and_strings',
    'intermediate',
    'advanced',
    'gui',
    'open_ended'
]

simple_problems = {}
for category in simple_categories:
    category_tag = Path('simple_programming_problems') / category

    simple_problems[category] = grab_unsolved_problems(category_tag)
# =============================================================================
