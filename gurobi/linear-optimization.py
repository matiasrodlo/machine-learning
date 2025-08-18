# -----------------------------------------------------------
# Linear Programming with Gurobi - Beginner Example
# -----------------------------------------------------------

# Step 1: Import gurobipy package
from gurobipy import *   # gives access to Gurobi classes and functions

# Step 2: Create an optimization model
# Think of this as your "workspace" where you define variables, objectives, and constraints
opt_mod = Model(name="linear program")

# Step 3: Add decision variables
# We create two variables, x and y
# vtype = GRB.CONTINUOUS → continuous (can be any real number)
# lb = 0 → non-negative (x, y ≥ 0)
x = opt_mod.addVar(name='x', vtype=GRB.CONTINUOUS, lb=0)
y = opt_mod.addVar(name='y', vtype=GRB.CONTINUOUS, lb=0)

# Step 4: Define the objective function
# Objective: minimize 5x + 4y
# GRB.MINIMIZE tells Gurobi this is a minimization problem
obj_fn = 5*x + 4*y
opt_mod.setObjective(obj_fn, GRB.MINIMIZE)

# Step 5: Add the constraints
# Constraints are "rules" the solution must satisfy
# c1: x + y ≥ 8
# c2: 2x + y ≥ 10
# c3: x + 4y ≥ 11
c1 = opt_mod.addConstr(x + y >= 8, name='c1')
c2 = opt_mod.addConstr(2*x + y >= 10, name='c2')
c3 = opt_mod.addConstr(x + 4*y >= 11, name='c3')

# Step 6: Solve the model
# optimize() runs the solver and finds the best values for x and y
opt_mod.optimize()

# Optional: write the model into a .lp file (text format) to inspect it
opt_mod.write("linear_model.lp")

# -----------------------------------------------------------
# After running, Gurobi will print the solution in the console:
# - Optimal values of x and y
# - The minimum value of the objective function (5x + 4y)
# -----------------------------------------------------------
 # Print solution values
 
if opt_mod.status == GRB.OPTIMAL:
    print(f"Optimal x = {x.X}")
    print(f"Optimal y = {y.X}")
    print(f"Objective value = {opt_mod.objVal}")
