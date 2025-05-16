
from problem_picker.constants import ROOT_DIR
from problem_picker.utils.grab_unsolved_problems import grab_unsolved_problems
from yaml import safe_load


def grab_pool_of_problems() -> dict[str, list[str] | dict[str, list[str]]]:
    '''
    Create a pool of problems to pick from, based on the predefined tags
    and their metadata settings.
    '''
    # Type tags for the program to know what it's working with
    tags: dict[str, dict[str, bool]]
    # Load the tags file
    path_to_tags = (ROOT_DIR / 'tags').with_suffix('.yaml')
    with path_to_tags.open('r', encoding='utf-8') as file:
        tags = safe_load(file)

    # The end result, typed for the program to know what it's working with
    problem_pool: dict[str, list[str] | dict[str, list[str]]] = dict()
    # Grab the problems dynamically
    for tag, flags in tags.items():
        # The name of the tag is the dir name
        tag_dir = ROOT_DIR / tag

        is_numbered = flags['numbered']

        # If the 'multiple_files' tag is true, grab the subdirs as separate
        #   targets, and create a dict of those problems
        if flags['multiple_files']:
            # Grab a list of the sub categories which are subdirectory names
            sub_categories = [p.name for p in tag_dir.iterdir() if p.is_dir()]

            for category in sub_categories:
                category_tag = f'{tag}/{category}'

                category_dir = tag_dir / category
                category_problems = grab_unsolved_problems(category_dir, is_numbered)

                problem_pool[category_tag] = category_problems
        # If the 'multiple_files' tag is false, then the dir is
        #   as far as we need to branch
        else:
            problem_pool[tag] = grab_unsolved_problems(tag_dir, is_numbered)

    return problem_pool
