import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.integrate import odeint
from scipy.integrate import solve_ivp


"""
Solves first order differential equations using scipy. Scipy has either odeint 
or solve_ivp for solving differential equations. Odeint is more general, 
solve_ivp has more versatility. 
"""
# Some DE
def dvdt(t, v):
    return 3*v**2 - 5

v0 = 0

# Solve 100 times between 0 and 1 (seconds)
t = np.linspace(0, 1, 100)

# odeint --> Takes in DE, initial condition(v0), t = times we want to sovle, tfirst = True b/c t comes first in DE
sol_m1 = odeint(dvdt, y0 = v0, t = t, tfirst = True)

# solve_ivp --> Takes in DE, t_span = how long you are solving it over, y0 = array v0, times to evaluate on
sol_m2 = solve_ivp(dvdt, t_span=(0,max(t)), y0=[v0], t_eval=t)

print("This is solution #1: ") 
# sol_m1.T[0] --> Tranposes array and gives the 0th quantity. This is useful if solving for y1, y2, y3 --> [0] [1] [2]
print(sol_m1)
print("This is solution #2: ")
# sol_m2.y gives solution 
print(sol_m2)

# Extracting solutions into a new variable
v_sol_m1 = sol_m1.T[0]
v_sol_m2 = sol_m2.y[0]

# Plots both solutions
"""
plt.plot(t, v_sol_m1)
plt.plot(t, v_sol_m2, '--')
plt.ylabel('$v(t)$', fontsize=22)
plt.xlabel('$t$', fontsize=22)
plt.show()
"""