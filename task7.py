import random
import matplotlib.pyplot as plt
from collections import defaultdict

# Кількість симуляцій
N = 1_000_000

def monte_carlo_simulation(n_simulations):
    results = defaultdict(int)
    for _ in range(n_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        results[total] += 1
    return results

def calculate_probabilities(results, n_simulations):
    return {k: v / n_simulations * 100 for k, v in sorted(results.items())}

def print_table(probabilities):
    print("Сума\tІмовірність (Монте-Карло)")
    for total, prob in probabilities.items():
        print(f"{total}\t{prob:.2f}%")

def plot_probabilities(probabilities):
    labels = list(probabilities.keys())
    values = list(probabilities.values())

    analytical = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }
    analytical_values = [analytical[sum_] for sum_ in labels]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, label='Монте-Карло', alpha=0.7)
    plt.plot(labels, analytical_values, 'r--', marker='o', label='Аналітична модель')
    plt.xlabel("Сума на кубиках")
    plt.ylabel("Імовірність (%)")
    plt.title("Імовірність сум при киданні двох кубиків (Метод Монте-Карло)")
    plt.xticks(labels)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    results = monte_carlo_simulation(N)
    probabilities = calculate_probabilities(results, N)
    print_table(probabilities)
    plot_probabilities(probabilities)