from .core.primitives import *
from .core.wrap_primitives import *
from .core.grad_map import grad_map #, gradient_of

from .random import random

def init_grad_map():
    from .core.diff_funcs import init_diff_funcs
    return

init_grad_map()