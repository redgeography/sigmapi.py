
"""
Allows you to create sigma/pi the mathematical way. e.g. from

6
Σ i
i = 1

to

sigma(
6,
lambda: i,
i = 1
)

or even add a step, the syntax for that is

sigma(
6,
lambda: i,
i = 1, step = 2
)

provides 2 functions: sigma() and pi().

you can `from sigmapi import *` to get the functions,

or even `from sigmapi import sigma, pi as piproduct` or some other name than
piproduct to prevent clashes with the constant named 'pi'

"""


__all__ = ["sigma", "pi"]

from types import CellType as cell, FunctionType as function


def inject(fn, varname):
    code = fn.__code__
    cll = cell()
    lcls = [ *code.co_freevars]
    cells = [] if fn.__closure__ is None else [*fn.__closure__]
    try:
        idx = lcls.index(varname)
        lcls.remove(idx)
        cells.remove(idx)
    except IndexError:
        pass
    
    lcls.insert(0, varname)
    cells.insert(0, cll)
    code = code.replace(co_freevars = (*lcls,))
    new = function(code, fn.__globals__, fn.__name__, fn.__argdefs__, (*cells,), fn.__kwdefaults__)
    return (new, cll)



def sigma(stop, func, /, *, step = 1, **var):
    (varname, start) = (*var.items(),)[0]
    (fnc, cll) = inject(func, varname)
    sum = 0
    for i in range(start, stop + step, step):
        cll.cell_contents = i
        sum += fnc()
        
    return sum




# just the sigma function modified for the product
# to minimize name clashes from the arbitrary variable declaration

def pi(stop, func, /, *, step = 1, **var):
    (varname, start) = (*var.items(),)[0]
    (fnc, cll) = inject(func, varname)
    prod = 1
    for i in range(start, stop + step, step):
        cll.cell_contents = i
        prod *= fnc()
        
    return prod
