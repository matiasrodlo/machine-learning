# -----------------------------------------------------------
# Classic Assignment Problem in Gurobi (4x4 example)
# Each worker i is assigned to at most one task j,
# and each worker must be assigned to exactly one task.
# Objective: minimize total assignment cost.
# -----------------------------------------------------------

# Step 1: Create input data (cost matrix)
import numpy as np
np.random.seed(42)  # optional: make results reproducible
cost = np.random.randint(1, 10, (4, 4))  # 4 workers x 4 tasks, costs in [1..9]

# Step 2: Import Gurobi
from gurobipy import Model, GRB, quicksum

# Step 3: Create the model
assignment_model = Model('Assignment')  # fixed typo in name

# Step 4: Decision variables
# x[i,j] = 1 if worker i is assigned to task j, 0 otherwise (binary)
I, J = cost.shape
x = assignment_model.addVars(I, J, vtype=GRB.BINARY, name="x")

# Step 5: Constraints

# (A) Workload: each task j is done by at most one worker (≤ 1)
#    For the classic square assignment, we usually set this to == 1.
#    Keeping ≤ 1 allows some tasks to remain unassigned (not typical for square case).
assignment_model.addConstrs(
    (quicksum(x[i, j] for i in range(I)) <= 1 for j in range(J)),
    name='workload'
)

# (B) Completion: each worker i must be assigned to exactly one task (== 1)
assignment_model.addConstrs(
    (quicksum(x[i, j] for j in range(J)) == 1 for i in range(I)),
    name='completion'
)

# Step 6: Objective — minimize total assignment cost
assignment_model.setObjective(
    quicksum(cost[i, j] * x[i, j] for i in range(I) for j in range(J)),
    GRB.MINIMIZE
)

# Step 7: Solve and inspect
assignment_model.setParam('OutputFlag', False)
assignment_model.optimize()

print('Model Statistics')
assignment_model.printStats()
print('\nModel summary\n')
assignment_model.display()

# Step 8: Print solution in a friendly way
if assignment_model.status == GRB.OPTIMAL:
    total_cost = assignment_model.objVal
    print(f'\nOptimal total cost: {total_cost:.2f}')
    print('Assignments (worker -> task, cost):')
    for i in range(I):
        for j in range(J):
            if x[i, j].X > 0.5:  # chosen
                print(f'  worker {i} -> task {j}  (cost={cost[i, j]})')
else:
    print(f'\nModel ended with status: {assignment_model.status}')
