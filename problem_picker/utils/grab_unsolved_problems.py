
from pathlib import Path
from problem_picker.utils.grab_list_of_problems import grab_list_of_problems


def grab_unsolved_problems(dir: Path, is_numbered: bool) -> list[str]:
    '''
    Grabs the list of problems to solve, and the problems that have
    been solved, and returns the problems left to solve.

    Args:
        dir (Path): The target directory.
        is_numbered (bool): Whether or not the problems are numbered.

    Returns:
        list[str]: The list of problems that still need to be solved.

    Notes:
        - The returned list of problems is sorted based on whether
        they are numbered or not.
    '''
    problems_file = (dir / 'problems').with_suffix('.txt')
    problems = grab_list_of_problems(problems_file)

    completed_file = (dir / 'complete').with_suffix('.txt')
    completed_problems = grab_list_of_problems(completed_file)

    unsolved_problems = list(set(problems) - set(completed_problems))

    if is_numbered:
        unsolved_problems.sort(key=lambda x: int(x.split('. ')[0]))
    else:
        unsolved_problems = sorted(unsolved_problems)

    return unsolved_problems
