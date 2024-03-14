# 8-15 Priting Models

def printing_functions(unprinted_designs, completed_models):
    """
    Simulate printing each design, untile none are left.
    Move each design to completed_models after printing
    :param unprinted_designs: a list
    :param completed_models: a list
    :return: a list
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print('\nThe following models have been designed:')
    for completed_model in completed_models:
        print(completed_model)