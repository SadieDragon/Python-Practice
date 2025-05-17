
from problem_picker.utils import PoolOfProblems


def pick_problems() -> None:
    '''
    Pick a set of 5 problems for the day.

    Notes:
        - A template directory is made for the selected problems.
        - Please put unsolved problems from each day into `unsolved.txt`.
        They will be recycled into the current day's choices, and their
        template directory will be removed.
        - 2 copies of the selected problems will be stored. One in a file for
        the daily log, and one in `current_day` in root for ease of access.
        On running this script, the previous day will have unsolved
        problems removed.
    '''
    # Generate the basic pool of problems
    pool_of_problems = PoolOfProblems().pool_of_problems

    print(pool_of_problems)
