#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Differential Equation Solver

@author: trevorharless
"""

"""
First section takes in an equation and solves for
the differential equation. Can also do initial
value problems.

Uses sympy library
"""

from sympy import *
import sympy as sp

# Creates x object and y object
x = sp.symbols('x')

# Creates the function object
f = sp.Function('f')(x)

# Creates a differential equation
diff_eq = Eq(f.diff(), (2*x + sp.sec(x)**2) / (2 * f))

# Solves the DE
sol = sp.dsolve(diff_eq, f)

# Display the differential equation
print("This is the DE that was inputted: ")
display(diff_eq)

# Display the solution to the DE
print("Solution(s) to the DE: ")
display(sol)

# Handling C1, C2, etc

# Expression of solution, right hand side of equation, 
# if it is a list get index of sol you want --> sol[0].rhs
#exp = sol.rhs

# Print right hand side of the solution
#print("This is the expression: ")
#display(exp)

# Gets the variables in the expression, in this case C1, C2
#C1, x = tuple(exp.free_symbols)

# Can set the values of C2 = 1, C1 = 0, and x = 10
# exp.subs({C1: 0, C2: 1, x: 10})

# Initial Value Problem

# First condition example is f(1) = 0
# Second condition example is f'(2) = 1
# ics = {f.subs(x, 1): 0, f.diff().subs(x, 2): 1}
ics = {f.subs(x, 0): -5}

# Solving an initial value problem
ivp = sp.dsolve(diff_eq, ics=ics)
print("This is the initial value solution: ")
display(ivp)

"""
Second section produces a numerical approximation 
of the analytic solution.

Uses scipy, nympy, and matplot libraries
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# Differential equation to be solved  
def dydt(t, y):
    return y**2 - 3

y0 = 0
# Solve 100 times between 0 and 1 --> .01 per
t = np.linspace(0, 1, 100)

"""
#odeint --> Takes in DE, initial condition(v0), t = times we want to solve, 
#tfirst = True b/c t comes first in DE
"""
sol_m1 = odeint(dydt, y0 = y0, t = t, tfirst = True)
print("This is the solution: ") 
print(sol_m1)

# Plots the solution
plt.plot(t, sol_m1)
plt.ylabel('$y(t)$', fontsize=20)
plt.xlabel('$t$', fontsize=20)
plt.show()