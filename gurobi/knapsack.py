# -----------------------------------------------------------
# 0/1 Knapsack Problem with Gurobi
# -----------------------------------------------------------

# Step 1: Create the data (weights and values)

w = [4, 2, 5, 4, 5, 1, 3, 5]      # weights of the 8 items
v = [10, 5, 18, 12, 15, 1, 2, 8]  # values (profits) of the 8 items
C = 15                            # capacity of the knapsack
N = len(w)                        # number of items

# Step 2: Import Gurobi package
from gurobipy import *

# Step 3: Create an optimization model
# This is our "workspace" where we will add variables, objective, and constraints
knapsack_model = Model('knapsack')

# Step 4: Add decision variables
# x[i] = 1 if item i is included in the knapsack, 0 otherwise
# Binary because items cannot be taken partially
x = knapsack_model.addVars(N, vtype=GRB.BINARY, name="x")

# Step 5: Define the objective function
# Maximize the total value of selected items: sum(v[i] * x[i])
obj_fn = sum(v[i] * x[i] for i in range(N))
knapsack_model.setObjective(obj_fn, GRB.MAXIMIZE)

# Step 6: Add the constraint
# Total weight of chosen items cannot exceed knapsack capacity
# sum(w[i] * x[i]) ≤ C
knapsack_model.addConstr(sum(w[i] * x[i] for i in range(N)) <= C)

# Step 7: Solve the model
# Turn off detailed solver output for cleaner results
knapsack_model.setParam('OutputFlag', False)
knapsack_model.optimize()

# Print the optimal objective value (max total value)
print('Optimization is done. Objective Function Value: %.2f' % knapsack_model.objVal)

# Step 8: Print the chosen items
# Loop through all decision variables and print their values (0 or 1)
for var in knapsack_model.getVars():
    print('%s: %g' % (var.varName, var.x))
