
from problem_picker.constants import ROOT_DIR
from yaml import safe_load

from problem_picker.utils.grab_unsolved_problems import grab_unsolved_problems


class PoolOfProblems:
    pool: dict[str, list[str]] = {}

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
            is_numbered = flags.get('numbered', False)

            # If there are multiple files, then use the names of the subdirs
            #   as keys, and the paths to them to grab the problems
            if flags.get('multiple_files', False):
                for subdir in tag_dir.iterdir():
                    # Skip any not directory
                    if not subdir.is_dir():
                        continue

                    # Generate the key name
                    subtag = f'{tag}/{subdir.name}'

                    # Generate the list of problems
                    self.pool[subtag] = grab_unsolved_problems(
                        subdir,
                        is_numbered
                        )

            # If there are not multiple files, then just use the tag as
            #   the key for the pool of problems
            else:
                self.pool[tag] = grab_unsolved_problems(tag_dir, is_numbered)
