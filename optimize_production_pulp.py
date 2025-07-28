import pulp
import pandas as pd

# === Step 1: Define Products and Material Usage ===

products = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Each list represents material usage for materials 1 to 6.
# Focus is on Material 3 (index 2) and Material 5 (index 4), which are limited.
material_usage = {
    'A': [1, 2, 3, 1, 2, 1],
    'B': [0, 1, 2, 2, 1, 1],
    'C': [2, 1, 1, 3, 3, 0],
    'D': [0, 0, 2, 1, 2, 1],
    'E': [1, 1, 2, 0, 2, 1],
    'F': [1, 2, 1, 0, 3, 0],
    'G': [1, 0, 2, 1, 1, 2],
    'H': [2, 2, 2, 0, 1, 1],
    'I': [0, 1, 3, 1, 2, 2],
    'J': [1, 1, 2, 2, 2, 1]
}

# Available stock of constrained materials.
available_materials = {
    'Material 3': 50,
    'Material 5': 40
}

# === Step 2: Create Optimization Model ===

# Define a maximization problem
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Create decision variables: how many units to produce of each product.
# All variables are integer and ≥ 0.
produce_vars = {
    product: pulp.LpVariable(f"Produce_{product}", lowBound=0, cat='Integer')
    for product in products
}

# Objective: Maximize the total number of units produced.
model += pulp.lpSum(produce_vars[p] for p in products), "Total_Units_Produced"

# Constraint for Material 3 usage.
model += pulp.lpSum(produce_vars[p] * material_usage[p][2] for p in products) <= available_materials['Material 3'], "Material3_Limit"

# Constraint for Material 5 usage.
model += pulp.lpSum(produce_vars[p] * material_usage[p][4] for p in products) <= available_materials['Material 5'], "Material5_Limit"

# === Step 3: Solve the Model ===

model.solve()

# === Step 4: Output the Results ===

# Print solution status
print(f"🧮 Optimization Status: {pulp.LpStatus[model.status]}")

# Extract and print results.
output = []
total_units = 0

print("\n Optimal Production Plan:\n")
for product in products:
    qty = produce_vars[product].varValue
    if qty > 0:
        print(f"Produce {int(qty)} units of Product {product}")
    output.append({'Product': product, 'Units to Produce': int(qty)})
    total_units += int(qty)

# Print total units.
print(f"\n🔢 Total Units Produced: {total_units}")

result_df = pd.DataFrame(output)
result_df.sort_values(by='Units to Produce', ascending=False, inplace=True)
result_df.reset_index(drop=True, inplace=True)

# Show result table (for Jupyter notebooks).
result_df
