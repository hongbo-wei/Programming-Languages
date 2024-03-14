# 8-12

def make_sandwich(*args):
    """An example of using arbitrary parameter"""
    print("The sandwich contains: ")
    for item in args:
        print(f'- {item}')


make_sandwich('tuna')
make_sandwich('egg', 'bacon', 'beef')
make_sandwich('tomato', 'beef', 'sausage', 'ketchup sauce')