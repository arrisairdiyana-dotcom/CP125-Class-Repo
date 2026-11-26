# Lab 01 Exercise 1: Road Trip Budgeter
def is_budget_sufficient (one_way_km,budget):
    distance = one_way_km * 2
    fuel_litre = distance / 10
    total_cost = fuel_litre * 2

    if total_cost <= budget :
        return True
    else:
        return False


print(is_budget_sufficient(100,40))
print(is_budget_sufficient(100,39))      