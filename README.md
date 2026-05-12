
sigmapi.py - Mathematical-like Σ (sigma/sum) and Π (pi/product)

## Main


Allows you to create sigma/pi the mathematical way. e.g. from
![A sigma function ( 6? )](assets/Sigma.png)

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
Provides 2 functions: `sigma()` and `pi()`.

you can `from sigmapi import *` to get the functions as global variables,

or even `from sigmapi import sigma, pi as piproduct` or some other name than
`piproduct` to prevent clashes with the constant named `pi`.

## Installation
First, install Git and PIP, if you haven't already.
Once installed, execute the command in your command prompt
```
pip install "git+https://github.com/redgeography/sigmapi.py.git#subdirectory=lib"
```
This will take it straight from this github repo, and install it. From there you can import via `import sigmapi` or better yet  `from sigmapi import * `.
