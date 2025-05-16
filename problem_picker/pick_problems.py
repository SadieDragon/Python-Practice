
from pathlib import Path
from problem_picker.constants import SIMPLE_CATEGORIES
from problem_picker.utils import grab_unsolved_problems


def pick_problems() -> None:
    '''
    Pick a set of 5 problems for the day.

    Notes:
        - Tags are generated from the constants file.
        - If a category is completed, please remove it from the tags list.
        - If a category is to be added, please add it following the previous
        template. (I do expect to add Euler one day.)
        - A template directory is made for the selected problems.
        - Please put unsolved problems from each day into `unsolved.txt`.
        They will be recycled into the current day's choices, and their
        template directory will be removed.
        - 2 copies of the selected problems will be stored. One in a file for
        the daily log, and one in `current_day` in root for ease of access.
        On running this script, the previous day will have unsolved
        problems removed.
    '''
    rosetta_problems = grab_unsolved_problems('rosetta_code')

    simple_problems = {}
    for category in SIMPLE_CATEGORIES:
        category_tag = Path('simple_programming_problems') / category

        simple_problems[category] = grab_unsolved_problems(category_tag)

    return [rosetta_problems, simple_problems]  # Temp
