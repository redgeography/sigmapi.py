
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

or even add a step like

sigma(
6,
lambda: i,
i = 1, step = 2
)
which isn't common math syntax but the thing is there *is* no common syntax
for that

provides 2 functions: sigma() and pi().

you can 'from sigmapi import *' to get the functions,

or even 'from sigmapi import sigma, pi as piproduct' or some other name than
piproduct to prevent clashes with the constant named 'pi'

"""


__all__ = ["sigma", "pi"]


def sigma(stop, func, *, step = 1, **var):
    (varname, start) = next(iter(var.items()))
    code = func.__code__
    closures = inspect.getclosurevars(func)
    glbls = closures.globals.copy()
    glbls.update(closures.builtins)
    lcls = closures.nonlocals.copy()
    sum = 0
    for i in range(start, stop + step, step):
        lcls[varname] = i
        sum += eval(code, glbls, lcls)
        
    return sum

def pi(stop, func, *, step = 1, **var):
    # just the sigma function modified for the product
    # to minimize name clashes from the arbitrary variable declaration
    (varname, start) = next(iter(var.items()))
    code = func.__code__
    closures = inspect.getclosurevars(func)
    glbls = closures.globals.copy()
    glbls.update(closures.builtins)
    lcls = closures.nonlocals.copy()
    prod = 1
    for i in range(start, stop + step, step):
        lcls[varname] = i
        prod *= eval(code, glbls, lcls)
        
    return prod
