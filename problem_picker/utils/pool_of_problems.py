
from pathlib import Path
from problem_picker.constants import ROOT_DIR
from yaml import safe_load


class PoolOfProblems:
    pool_of_problems: dict[str, list[str]] = {}

    is_numbered: bool

    def __init__(self) -> None:
        '''
        Gather the list of problems that need to be solved.
        '''
        # Load the tags for the problems
        tags_path = ROOT_DIR / 'tags.yaml'
        with tags_path.open('r', encoding='utf-8') as file:
            tags: dict[str, dict[str, bool]] = safe_load(file)

        # Go through the tags list and populate the pool
        for tag, flags in tags.items():
            # The base dir for the tag is the name appended to root
            tag_dir = ROOT_DIR / tag

            # Unpack the numbered flag, defaulting to False for safety
            self.is_numbered = flags.get('numbered', False)

            # If there are not multiple files, then simply generate the
            #   pool of problems and move on
            if not flags.get('multiple_files', False):
                self.grab_unsolved_problems(tag_dir)
                continue

            # If there are multiple files, then go through the parent
            #   list of subdirs to get their pool of items
            for subdir in tag_dir.iterdir():
                # Skip any loose files
                if not subdir.is_dir():
                    continue

                # Generate the list of problems
                self.grab_unsolved_problems(subdir)

    @staticmethod
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
            - Skips any empty lines.
        '''
        # Use list comprehension to more easily generate the list
        #   of problems cleaned up, skipping empty lines, if the
        #   file exists
        try:
            with file_path.open('r', encoding='utf-8') as file:
                return [line.strip() for line in file if line.strip()]
        # If the file does not exist, or is lost, then just return an
        #   empty list
        except FileNotFoundError:
            return []

    def grab_unsolved_problems(self, target_dir: Path) -> None:
        '''
        Grabs the list of problems to solve, and the problems that have
        been solved, and returns the problems left to solve.

        Args:
            target_dir (Path): The target directory to grab the problems from.

        Returns:
            list[str]: The list of problems that still need to be solved.

        Notes:
            - The flag for numbered is a class variable.
            - The returned list of problems is sorted based on whether
            they are numbered or not.
        '''
        # Determine the key for the pool of items by just grabbing the
        #   name of the target dir
        problem_set_name = target_dir.name

        # Grab the problems that need to be solved
        problems_file = target_dir / 'problems.txt'
        problems = self.grab_list_of_problems(problems_file)

        # Grab the problems that have been solved
        completed_file = target_dir / 'complete.txt'
        completed_problems = self.grab_list_of_problems(completed_file)

        # Remove the solved problems from the list
        unsolved_problems = list(set(problems) - set(completed_problems))

        # Sort the problems, based on if they are numbered or not
        if self.is_numbered:
            unsolved_problems.sort(key=lambda x: int(x.split('. ')[0]))
        else:
            unsolved_problems = sorted(unsolved_problems)

        # Store the problems in the pool
        self.pool_of_problems[problem_set_name] = unsolved_problems
