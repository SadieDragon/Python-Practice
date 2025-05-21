
# I have already done something similar; thus this is modified code
#   to fit the prompt a little better. Some pre-configured maths tho.

TARGET = 12


def int_x_wide(n: int, width: int = 4) -> str:
    '''
    A wrapper function for formatting an int into a str with a set width.

    Args:
        n (int): The integer to be formatted into a str.
        width (int): How wide that str is to be padded to. (Default: 4)

    Returns:
        str: The formatted int.
    '''
    return f'{n:{width}}'


# Range of numbers 1-12
one_to_twelve = range(1, (TARGET + 1))

# Header row (first factors)
print('   |' + ''.join(int_x_wide(i) for i in one_to_twelve))

# Separator line
print('-' * ((TARGET * 4) + (TARGET // 2)))

# Rows
for i in one_to_twelve:
    # The column indicating the second factor
    first_column = f'{int_x_wide(i, 2)} |'

    # Calculate the list of products
    products = [(i * j) for j in one_to_twelve]

    # Format them
    formatted = ''.join(int_x_wide(product) for product in products)

    # Print the row
    print(f'{first_column}{formatted}')
