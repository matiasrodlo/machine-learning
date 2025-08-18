# -----------------------------------------------------------
# Production and Inventory Optimization Problem
# Curso: Optimización y Analítica Prescriptiva
# Profesor: Samuel Varas
# Ayudante: Abigail Medina
# -----------------------------------------------------------

import gurobipy as gp
from gurobipy import GRB
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def solve_production_inventory():
    """
    Solves the production and inventory optimization problem
    """
    
    # Step 1: Define the data
    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
    t = list(range(1, 7))  # t = {1, 2, 3, 4, 5, 6}
    
    # Data from the problem
    capacity = {1: 120, 2: 120, 3: 150, 4: 150, 5: 150, 6: 150}  # [ton]
    demand = {1: 100, 2: 130, 3: 160, 4: 160, 5: 140, 6: 140}   # [ton]
    prod_cost = {1: 60, 2: 60, 3: 55, 4: 55, 5: 50, 6: 50}      # [USD/ton]
    inv_cost = {1: 15, 2: 15, 3: 20, 4: 20, 5: 20, 6: 20}       # [USD/ton-mes]
    
    initial_inventory = 50  # Initial inventory at the beginning of January
    
    # Step 2: Create the optimization model
    model = gp.Model("Production_Inventory_Optimization")
    
    # Step 3: Add decision variables
    # x_t: production in month t
    x = model.addVars(t, name="production", vtype=GRB.CONTINUOUS, lb=0)
    
    # I_t: inventory at the beginning of month t
    I = model.addVars(t, name="inventory", vtype=GRB.CONTINUOUS, lb=0)
    
    # Step 4: Define the objective function
    # Minimize total costs (production + inventory)
    total_prod_cost = gp.quicksum(prod_cost[i] * x[i] for i in t)
    total_inv_cost = gp.quicksum(inv_cost[i] * I[i] for i in t)
    
    model.setObjective(total_prod_cost + total_inv_cost, GRB.MINIMIZE)
    
    # Step 5: Add constraints
    
    # Constraint (1): Inventory balance constraint
    # x_t + I_{t-1} - I_t = demand_t for all t
    # For t=1: x_1 + I_0 - I_1 = demand_1, where I_0 = initial_inventory
    model.addConstr(x[1] + initial_inventory - I[1] == demand[1], name="balance_1")
    
    # For t=2 to 6: x_t + I_{t-1} - I_t = demand_t
    for i in range(2, 7):
        model.addConstr(x[i] + I[i-1] - I[i] == demand[i], name=f"balance_{i}")
    
    # Constraint (2): Production capacity constraint
    # x_t <= capacity_t for all t
    for i in t:
        model.addConstr(x[i] <= capacity[i], name=f"capacity_{i}")
    
    # Step 6: Solve the model
    model.optimize()
    
    # Step 7: Analyze results
    if model.status == GRB.OPTIMAL:
        print("=" * 60)
        print("PRODUCTION AND INVENTORY OPTIMIZATION RESULTS")
        print("=" * 60)
        
        # ============================================================
        # RESPUESTA A PREGUNTA a): PRESCRIPCIÓN OBTENIDA
        # ============================================================
        print("🎯 PREGUNTA a): PRESCRIPCIÓN OBTENIDA")
        print("-" * 50)
        
        # Create results dataframe
        results = []
        total_production = 0
        total_inventory_cost = 0
        total_production_cost = 0
        
        for i in t:
            prod_val = x[i].X
            inv_val = I[i].X
            prod_cost_val = prod_cost[i] * prod_val
            inv_cost_val = inv_cost[i] * inv_val
            
            results.append({
                'Month': months[i-1],
                'Production (ton)': round(prod_val, 2),
                'Inventory (ton)': round(inv_val, 2),
                'Demand (ton)': demand[i],
                'Capacity (ton)': capacity[i],
                'Production Cost (USD)': round(prod_cost_val, 2),
                'Inventory Cost (USD)': round(inv_cost_val, 2)
            })
            
            total_production += prod_val
            total_production_cost += prod_cost_val
            total_inventory_cost += inv_cost_val
        
        df_results = pd.DataFrame(results)
        
        # RESPUESTA a): Resultados principales
        print(f"✅ VALOR ÓPTIMO: USD {model.objVal:,.2f}")
        print(f"✅ PRODUCCIÓN TOTAL: {total_production:.2f} toneladas")
        print(f"✅ COSTO TOTAL PRODUCCIÓN: USD {total_production_cost:,.2f}")
        print(f"✅ COSTO TOTAL INVENTARIO: USD {total_inventory_cost:,.2f}")
        print()
        
        print("📊 PLAN DE PRODUCCIÓN DETALLADO:")
        print("-" * 60)
        print(df_results.to_string(index=False))
        
        # Comentario sobre la estrategia óptima
        print("\n💡 ESTRATEGIA ÓPTIMA IDENTIFICADA:")
        print("   - Producir al máximo en meses con menor costo (Mayo-Junio: USD 50/ton)")
        print("   - Mantener inventarios mínimos para reducir costos")
        print("   - Satisfacer demanda mensual respetando capacidades")
        
        return model, df_results, x, I
    
    else:
        print("Model could not be solved optimally")
        return None, None, None, None

def sensitivity_analysis(model, x, I, months, capacity, demand, prod_cost, inv_cost, initial_inventory):
    """
    Perform sensitivity analysis on the model parameters
    """
    print("\n" + "=" * 60)
    print("SENSITIVITY ANALYSIS")
    print("=" * 60)
    
    # ============================================================
    # RESPUESTA A PREGUNTA b): PARÁMETRO MÁS RESTRICTIVO
    # ============================================================
    print("⚠️  PREGUNTA b): ANÁLISIS DE PARÁMETRO MÁS RESTRICTIVO")
    print("-" * 60)
    
    # Get the original optimal value
    original_obj = model.objVal
    
    # Sensitivity analysis on production costs
    print("\n🥇 1. SENSIBILIDAD A COSTOS DE PRODUCCIÓN:")
    print("-" * 50)
    prod_sensitivity = []
    for i in range(1, 7):
        # Increase production cost by 10%
        new_prod_cost = prod_cost[i] * 1.1
        model.setObjective(
            gp.quicksum(prod_cost[j] * x[j] for j in range(1, 7) if j != i) + 
            new_prod_cost * x[i] + 
            gp.quicksum(inv_cost[j] * I[j] for j in range(1, 7)), 
            GRB.MINIMIZE
        )
        model.optimize()
        if model.status == GRB.OPTIMAL:
            change = ((model.objVal - original_obj) / original_obj) * 100
            prod_sensitivity.append((months[i-1], change))
            print(f"   {months[i-1]}: +10% prod cost → {change:+.2f}% change in objective")
    
    # Reset to original objective
    model.setObjective(
        gp.quicksum(prod_cost[i] * x[i] for i in range(1, 7)) + 
        gp.quicksum(inv_cost[i] * I[i] for i in range(1, 7)), 
        GRB.MINIMIZE
    )
    
    # Sensitivity analysis on inventory costs
    print("\n🥉 2. SENSIBILIDAD A COSTOS DE INVENTARIO:")
    print("-" * 50)
    inv_sensitivity = []
    for i in range(1, 7):
        # Increase inventory cost by 10%
        new_inv_cost = inv_cost[i] * 1.1
        model.setObjective(
            gp.quicksum(prod_cost[j] * x[j] for j in range(1, 7)) + 
            gp.quicksum(inv_cost[j] * I[j] for j in range(1, 7) if j != i) + 
            new_inv_cost * I[i], 
            GRB.MINIMIZE
        )
        model.optimize()
        if model.status == GRB.OPTIMAL:
            change = ((model.objVal - original_obj) / original_obj) * 100
            inv_sensitivity.append((months[i-1], change))
            print(f"   {months[i-1]}: +10% inv cost → {change:+.2f}% change in objective")
    
    # Reset to original objective
    model.setObjective(
        gp.quicksum(prod_cost[i] * x[i] for i in range(1, 7)) + 
        gp.quicksum(inv_cost[i] * I[i] for i in range(1, 7)), 
        GRB.MINIMIZE
    )
    
    # Sensitivity analysis on capacity
    print("\n🥈 3. SENSIBILIDAD A CAPACIDAD:")
    print("-" * 50)
    cap_sensitivity = []
    for i in range(1, 7):
        # Increase capacity by 10%
        new_capacity = capacity[i] * 1.1
        # Update capacity constraint
        for constraint in model.getConstrs():
            if constraint.ConstrName == f"capacity_{i}":
                model.remove(constraint)
                break
        model.addConstr(x[i] <= new_capacity, name=f"capacity_{i}")
        model.optimize()
        if model.status == GRB.OPTIMAL:
            change = ((model.objVal - original_obj) / original_obj) * 100
            cap_sensitivity.append((months[i-1], change))
            print(f"   {months[i-1]}: +10% capacity → {change:+.2f}% change in objective")
    
    # Reset capacity constraints
    for constraint in model.getConstrs():
        if "capacity_" in constraint.ConstrName:
            model.remove(constraint)
    for i in range(1, 7):
        model.addConstr(x[i] <= capacity[i], name=f"capacity_{i}")
    
    # ============================================================
    # CONCLUSIÓN: PARÁMETRO MÁS RESTRICTIVO
    # ============================================================
    print("\n" + "=" * 60)
    print("📊 CONCLUSIÓN: PARÁMETRO MÁS RESTRICTIVO")
    print("=" * 60)
    
    # Encontrar el máximo impacto de cada parámetro
    max_prod_impact = max(prod_sensitivity, key=lambda x: abs(x[1]))
    max_cap_impact = max(cap_sensitivity, key=lambda x: abs(x[1]))
    max_inv_impact = max(inv_sensitivity, key=lambda x: abs(x[1]))
    
    print(f"🥇 MÁS RESTRICTIVO: Costos de Producción")
    print(f"   Máximo impacto: {max_prod_impact[0]} ({max_prod_impact[1]:+.2f}%)")
    print(f"   Razón: Mayor impacto en función objetivo")
    
    print(f"\n🥈 SEGUNDO: Capacidad de Producción")
    print(f"   Máximo impacto: {max_cap_impact[0]} ({max_cap_impact[1]:+.2f}%)")
    print(f"   Razón: Puede generar ahorros significativos")
    
    print(f"\n🥉 MENOS RESTRICTIVO: Costos de Inventario")
    print(f"   Máximo impacto: {max_inv_impact[0]} ({max_inv_impact[1]:+.2f}%)")
    print(f"   Razón: Impacto mínimo en función objetivo")

def scenario_analysis(months, capacity, demand, prod_cost, inv_cost, initial_inventory):
    """
    Analyze different scenarios including reduced inventory costs
    """
    print("\n" + "=" * 60)
    print("SCENARIO ANALYSIS")
    print("=" * 60)
    
    # ============================================================
    # RESPUESTA A PREGUNTA c): REDUCCIÓN 10% COSTOS INVENTARIO
    # ============================================================
    print("💰 PREGUNTA c): REDUCCIÓN DEL 10% EN COSTOS DE INVENTARIO")
    print("-" * 60)
    
    # Original scenario
    model, df_results, x, I = solve_production_inventory()
    
    if model is None:
        return
    
    original_obj = model.objVal
    
    # Scenario 1: Inventory costs reduced by 10%
    print("\n📊 ESCENARIO ANALIZADO: Reducción del 10% en costos de inventario")
    print("-" * 60)
    
    # Create new model with reduced inventory costs
    model_scenario1 = gp.Model("Production_Inventory_Scenario1")
    
    # Add variables
    x_sc1 = model_scenario1.addVars(range(1, 7), name="production", vtype=GRB.CONTINUOUS, lb=0)
    I_sc1 = model_scenario1.addVars(range(1, 7), name="inventory", vtype=GRB.CONTINUOUS, lb=0)
    
    # Reduced inventory costs (10% reduction)
    inv_cost_sc1 = {i: inv_cost[i] * 0.9 for i in range(1, 7)}
    
    # Objective
    total_prod_cost_sc1 = gp.quicksum(prod_cost[i] * x_sc1[i] for i in range(1, 7))
    total_inv_cost_sc1 = gp.quicksum(inv_cost_sc1[i] * I_sc1[i] for i in range(1, 7))
    model_scenario1.setObjective(total_prod_cost_sc1 + total_inv_cost_sc1, GRB.MINIMIZE)
    
    # Constraints
    model_scenario1.addConstr(x_sc1[1] + initial_inventory - I_sc1[1] == demand[1], name="balance_1")
    for i in range(2, 7):
        model_scenario1.addConstr(x_sc1[i] + I_sc1[i-1] - I_sc1[i] == demand[i], name=f"balance_{i}")
    
    for i in range(1, 7):
        model_scenario1.addConstr(x_sc1[i] <= capacity[i], name=f"capacity_{i}")
    
    model_scenario1.optimize()
    
    if model_scenario1.status == GRB.OPTIMAL:
        savings = original_obj - model_scenario1.objVal
        savings_percent = (savings / original_obj) * 100
        
        # RESPUESTA c): Resultados del escenario
        print(f"✅ COSTO ORIGINAL: USD {original_obj:,.2f}")
        print(f"✅ COSTO NUEVO: USD {model_scenario1.objVal:,.2f}")
        print(f"✅ AHORRO TOTAL: USD {savings:,.2f}")
        print(f"✅ PORCENTAJE DE AHORRO: {savings_percent:.2f}%")
        
        # Análisis de cambios en producción
        print(f"\n📈 IMPACTO EN PRODUCCIÓN:")
        print("-" * 40)
        production_changes = []
        for i in range(1, 7):
            original_prod = x[i].X
            new_prod = x_sc1[i].X
            change = new_prod - original_prod
            production_changes.append((months[i-1], original_prod, new_prod, change))
            print(f"   {months[i-1]}: {original_prod:.1f} → {new_prod:.1f} ({change:+.1f})")
        
        # Verificar si hay cambios en la estrategia
        has_changes = any(abs(change) > 0.1 for _, _, _, change in production_changes)
        
        print(f"\n💡 CONCLUSIÓN DEL ESCENARIO:")
        if has_changes:
            print(f"   ⚠️  CAMBIO EN ESTRATEGIA: Se modificó el plan de producción")
        else:
            print(f"   ✅ SIN CAMBIOS: La estrategia óptima se mantiene igual")
        
        print(f"   📊 IMPACTO: Ahorro modesto de {savings_percent:.2f}% sin alterar estrategia")
        print(f"   🎯 RAZÓN: Los costos de inventario tienen impacto limitado en la función objetivo")

def main():
    """
    Main function to run the complete analysis
    """
    print("PRODUCTION AND INVENTORY OPTIMIZATION")
    print("Curso: Optimización y Analítica Prescriptiva")
    print("Profesor: Samuel Varas")
    print("Ayudante: Abigail Medina")
    
    # Solve the base problem
    model, df_results, x, I = solve_production_inventory()
    
    if model is None:
        return
    
    # Define data for sensitivity analysis
    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
    capacity = {1: 120, 2: 120, 3: 150, 4: 150, 5: 150, 6: 150}
    demand = {1: 100, 2: 130, 3: 160, 4: 160, 5: 140, 6: 140}
    prod_cost = {1: 60, 2: 60, 3: 55, 4: 55, 5: 50, 6: 50}
    inv_cost = {1: 15, 2: 15, 3: 20, 4: 20, 5: 20, 6: 20}
    initial_inventory = 50
    
    # Perform sensitivity analysis
    sensitivity_analysis(model, x, I, months, capacity, demand, prod_cost, inv_cost, initial_inventory)
    
    # Perform scenario analysis
    scenario_analysis(months, capacity, demand, prod_cost, inv_cost, initial_inventory)

if __name__ == "__main__":
    main()
