
from problem_picker.constants import ROOT_DIR
from problem_picker.utils.grab_list_of_problems import grab_list_of_problems


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

    # Grab the list of unique elements
    unique_list = list(set(problems) - set(completed_problems))

    # If for rosetta, sort the list and return it as is
    if tag == 'rosetta_code':
        return sorted(unique_list)

    # For simple programming problems, each list of problems has the
    #   format `1. [problem]...`, and thus needs to be sorted by the
    #   number of problem instead of the first letter.
    # However, `.sort` returns `None`, so this cannot be one line.
    unique_list.sort(key=lambda x: int(x.split('. ')[0]))
    return unique_list
