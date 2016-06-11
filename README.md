# Numerical Calculation

* Linear fit: Performs the linear adjustment with two variables
* Trapezoidal rule: Calculates the area of a function by the trapezoidal rule
* Bisection method: Finds the first 'zero' point in the range

![Linear Fit](https://raw.githubusercontent.com/kayroncabral/numerical-calculation/master/images/linear-fit.png "Linear fit")

> python linearfit.py ``<start,stop>`` ``<function>``

- ``<start,stop>``: range of values to x
- ``<function>``: funcion to generate y values

e.g:
> python linearfit.py 0,5 "sin(x)"

![Trapezoidal Rule](https://raw.githubusercontent.com/kayroncabral/numerical-calculation/master/images/trapezoidal-rule.png "Trapezoidal rule")

> python trapezoidal.py ``<iteration>`` ``<start,stop>`` ``<function>``

- ``<iteration>``: number of iterations
- ``<start,stop>``: range of values to x
- ``<function>``: funcion to generate y values

e.g:
> python trapezoidal.py 20 0,5 "exp(x)"

![Bisection Method](https://raw.githubusercontent.com/kayroncabral/numerical-calculation/master/images/bisection-method.png "Bisection method")

> python bisection.py ``<iteration>`` ``<start,stop,distance>`` ``<function>``

- ``<iteration>``: number of iterations
- ``<start,stop,distance>``: range of values to x and distance between values
- ``<function>``: funcion to generate y values

e.g:
> python bisection.py 100 -5,5,0.01 "cos(x)"
