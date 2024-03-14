from printing_functions import printing_functions as pf
from printing_functions import show_completed_models as scm
# from printing_functions import *

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_model = []

pf(unprinted_designs, completed_model)
scm(completed_model)