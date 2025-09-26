def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left
    Move each design to completed_models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_models(completed_models):
    """ Display all competed models"""
    for model in completed_models:
        print(model)


# Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print("\nRunning")
print_models(unprinted_designs, completed_models)
print("\nThe following models have been printed:")
show_models(completed_models)