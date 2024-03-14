# 8-3
# 8-4 default value in parameter


def make_shirt(size='l', print_text='I love Python'):
    """An example of setting default value for a parameter in a function"""
    print(f'The size of the shirt is {size.upper()}')
    print('The following text will be printed on the shirt: ')
    print(f'\t{print_text}')


# call function using Positional Arguments
make_shirt('m', 'YOLO')

# call function using Keyword Arguments
make_shirt(print_text='Smile', size='l')

# 8-4
# Make a large shirt with default message
make_shirt()
# Make a medium shirt with default message
make_shirt('m')
# Make a shirt of any size with a different message
make_shirt(print_text='Hello World')

