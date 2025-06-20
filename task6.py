items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    # Сортуємо за співвідношенням калорій до вартості (найбільше — найкраще)
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    total_cost = 0
    chosen_items = []

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            chosen_items.append(name)
            total_cost += data["cost"]

    return chosen_items


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    # Створюємо таблицю dp[n+1][budget+1]
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    # Відновлюємо набір обраних страв
    chosen_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = names[i - 1]
            chosen_items.append(name)
            b -= items[name]["cost"]

    return chosen_items[::-1]  # щоб отримати в порядку вибору


if __name__ == "__main__":
    budget = 100

    print("=== Жадібний алгоритм ===")
    greedy = greedy_algorithm(items, budget)
    print("Обрані страви:", greedy)

    print("\n=== Динамічне програмування ===")
    dp = dynamic_programming(items, budget)
    print("Обрані страви:", dp)