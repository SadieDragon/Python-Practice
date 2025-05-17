
from collections import defaultdict
from problem_picker.constants import ROOT_DIR


def grab_unsolved_problems() -> dict[str, list[str]]:
    '''
    Grabs the list of problems that were unused from the previous day.

    Notes:
        - The file for unsolved problems is assumed to be in the root dir.
        - Format is expected as: '<set> | <problem>'
    '''
    # Generate the path to the file
    unsolved_problems_file = ROOT_DIR / 'unsolved.txt'

    # Try to open the file and extract the problems
    try:
        # Initiate the dict with each key defaulting its val to an empty list
        unsolved_problems: dict[str, list[str]] = defaultdict(list)

        with unsolved_problems_file.open('r', encoding='utf-8') as file:
            for line in file:
                # Skip any lines which do not have the expected format
                if ' | ' not in line:
                    continue

                # Split the problem set from the problem (only split once)
                problem_set, problem = line.strip().split(' | ', 1)

                # Store the problem in the pool
                unsolved_problems[problem_set].append(problem)

        # Return the dict as a normal instead of default
        return dict(unsolved_problems)

    # If the file was not found, just return an empty dict
    except FileNotFoundError:
        return {}
