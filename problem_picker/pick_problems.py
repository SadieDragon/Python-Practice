
from pathlib import Path
from problem_picker.constants import SIMPLE_CATEGORIES
from problem_picker.utils import grab_unsolved_problems


def pick_problems() -> list:
    '''
    Pick a list of problems for the day.

    Returns:
        list[str]: The problems to solve for the day.
    '''
    rosetta_problems = grab_unsolved_problems('rosetta_code')

    simple_problems = {}
    for category in SIMPLE_CATEGORIES:
        category_tag = Path('simple_programming_problems') / category

        simple_problems[category] = grab_unsolved_problems(category_tag)

    return [rosetta_problems, simple_problems]  # Temp
