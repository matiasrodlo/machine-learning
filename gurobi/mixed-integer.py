# -----------------------------------------------------------
# Mixed-Integer Linear Programming (MILP) Example in Gurobi
# -----------------------------------------------------------

# Step 1: Import gurobipy package
# This library provides all Gurobi functions, classes, and constants (like GRB)
from gurobipy import *

# Step 2: Create an optimization model
# "milp" is just the name of this optimization problem
milp_model = Model("milp")

# Step 3: Add decision variables
# Decision variables are the "unknowns" that the solver will decide.
# Each one has a type (binary, continuous, integer) and bounds.

# Binary variable: x can only be 0 or 1 (yes/no decision)
x = milp_model.addVar(vtype=GRB.BINARY, name="x")

# Continuous variable: y can take any real number >= 0
y = milp_model.addVar(vtype=GRB.CONTINUOUS, lb=0, name="y")

# Integer variable: z must be a whole number >= 0
z = milp_model.addVar(vtype=GRB.INTEGER, lb=0, name="z")

# Step 4: Define the objective function
# Objective: maximize 2x + y + 3z
# GRB.MAXIMIZE tells the solver this is a maximization problem
obj_fn = 2 * x + y + 3 * z
milp_model.setObjective(obj_fn, GRB.MAXIMIZE)

# Step 5: Add the constraints
# Constraints are "rules" that the solution must satisfy.

# Constraint 1: x + 2y + z ≤ 4
c1 = milp_model.addConstr(x + 2 * y + z <= 4, "c1")

# Constraint 2: 2z + y ≤ 5
c2 = milp_model.addConstr(2 * z + y <= 5, "c2")

# Constraint 3: x + y ≥ 1
c3 = milp_model.addConstr(x + y >= 1, "c3")

# Step 6: Solve the model
# This runs Gurobi’s solver to find the best values of x, y, and z
milp_model.optimize()

# Optional: print results if an optimal solution is found
if milp_model.status == GRB.OPTIMAL:
    print("\nOptimal solution found:")
    print(f"x = {x.X}")
    print(f"y = {y.X}")
    print(f"z = {z.X}")
    print(f"Objective value = {milp_model.objVal}")
