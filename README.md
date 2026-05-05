# sigmapi.py


Allows you to create sigma/pi the mathematical way. e.g. from
![A sigma function ( 6? )](Sigma.png)

to

```
sigma(
6,
lambda: i,
i = 1
)
```

or even add a step like
```
sigma(
6,
lambda: i,
i = 1, step = 2
)
```
which isn't common math syntax but the thing is there *is* no common syntax
for that.

Provides 2 functions: `sigma()` and `pi()`.

you can `from sigmapi import *` to get the functions as global variables,

or even `from sigmapi import sigma, pi as piproduct` or some other name than
`piproduct` to prevent clashes with the constant named `pi`


        prod *= eval(code, glbls, lcls)
        
    return prod
