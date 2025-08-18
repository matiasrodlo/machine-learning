# -----------------------------------------------------------
# Mixed-Integer Quadratic Program (MIQP) + Quadratic Constraint (MIQCP)
# -----------------------------------------------------------

# Step 1: Import Gurobi package
from gurobipy import *

# Step 2: Create a model
quadratic_model = Model('quadratic')

# Step 3: Define decision variables
# x = continuous >= 0
x = quadratic_model.addVar(vtype=GRB.CONTINUOUS, lb=0, name="x")
# y = integer >= 0
y = quadratic_model.addVar(vtype=GRB.INTEGER, lb=0, name="y")
# z = binary (0 or 1)
z = quadratic_model.addVar(vtype=GRB.BINARY, lb=0, name="z")

# Step 4: Add linear constraints
# c1: x + 3y + 2z >= 5
quadratic_model.addConstr(x + 3*y + 2*z >= 5, name="c1")
# c2: y + z >= 2.5
quadratic_model.addConstr(y + z >= 2.5, name="c2")

# Step 5: Define a quadratic objective
# Minimize x^2 + y^2 + z (z is binary, so z^2 == z, using z is fine)
obj_fn = x*x + y*y + z
quadratic_model.setObjective(obj_fn, GRB.MINIMIZE)

# Step 6: Solve the model (first solve, without the quadratic constraint)
quadratic_model.setParam('OutputFlag', False)  # suppress detailed logs
quadratic_model.optimize()

print('--- First solve (no quadratic constraint) ---')
if quadratic_model.status == GRB.OPTIMAL:
    print('Objective Value: %.6f' % quadratic_model.objVal)
    for var in quadratic_model.getVars():
        print(f'{var.varName} = {var.X:g}')
else:
    print(f'Status: {quadratic_model.status}')

# Step 7: Add a quadratic constraint and resolve
# Quadratic constraint (convex SOC form): y^2 + z^2 <= x^2
# Because z is binary, z^2 == z, so this is effectively y^2 + z <= x^2.
# Geometrically: ||(y, z)||_2 <= x, which is convex (second-order cone).
qc = quadratic_model.addConstr(y*y + z*z <= x*x, name="qc1")

# Re-optimize with the new constraint active
quadratic_model.optimize()

print('\n--- Second solve (with quadratic constraint qc1) ---')
if quadratic_model.status == GRB.OPTIMAL:
    print('Objective Value: %.6f' % quadratic_model.objVal)
    for var in quadratic_model.getVars():
        print(f'{var.varName} = {var.X:g}')
else:
    print(f'Status: {quadratic_model.status}')
