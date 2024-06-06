def greedy_algorithm(items, budget):
    
    mod = budget
    
    sorted_items = sorted(items.items(), key=lambda x: -x[1]['calories']/x[1]['cost'])
    
    output = {}
    total_calories = 0
    total_cost = 0
    
    for product, prop in sorted_items:
        if prop['cost'] > mod:
            continue

        output[product] = 1

        mod -= prop['cost']

        total_calories += prop['calories']
        total_cost += prop['cost']

    return {
        'selection': output,
        'cost': total_cost,
        'calories': total_calories
    }
    
def dynamic_programming(items, budget):
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]
    
    for i, (item, info) in enumerate(items.items()):
        cost = info["cost"]
        calories = info["calories"]
        for j in range(1, budget + 1):
            if cost <= j:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - cost] + calories/cost)
            else:
                dp[i + 1][j] = dp[i][j]
    
    selected_items = []
    i, j = len(items), budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[selected_items[-1]]["cost"]
        i -= 1
    
    selected_items.reverse()
    
    return {
        "selected_items": selected_items,
        "total_cost": sum([info["cost"] for product, info in items.items() if product in selected_items]),
        "total_calories": sum([info["calories"] for product, info in items.items() if product in selected_items])
    }

    
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
print()
print("greedy: ")
print()
print(greedy_algorithm(items, 100))
print()
print("dynamic: ")
print()
print(dynamic_programming(items, 100))
print()