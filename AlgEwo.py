import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def fitness_function(x):
    return np.sin(0.5 * x) + np.cos(0.75 * x)


def evolutionary_algorithm():
    population_size = 100  # Rozmiar populacji
    generations = 50  # Liczba generacji
    mutation_rate = 0.1  # Współczynnik mutacji

    # Inicjalizacja populacji początkowej
    population = np.random.uniform(low=-10, high=10, size=(population_size,))
    fitness_values = fitness_function(population)

    best_fitness_values = []
    std_deviations = []

    # Pętla główna algorytmu ewolucyjnego
    for _ in range(generations):
        # Selekcja rodziców
        parents_indices = np.random.choice(range(population_size), size=2, replace=False)
        parent1 = population[parents_indices[0]]
        parent2 = population[parents_indices[1]]

        # Krzyżowanie rodziców
        offspring = 0.5 * (parent1 + parent2)

        # Mutacja potomka
        if np.random.rand() < mutation_rate:
            offspring += np.random.normal(scale=0.1)

        offspring_fitness = fitness_function(offspring)

        # Aktualizacja populacji
        min_fitness_index = np.argmin(fitness_values)
        population[min_fitness_index] = offspring
        fitness_values[min_fitness_index] = offspring_fitness

        # Zapis najlepszego rozwiązania
        best_solution_index = np.argmin(fitness_values)
        best_fitness_values.append(fitness_values[best_solution_index])

        # Obliczanie odchylenia standardowego
        std_deviation = np.std(fitness_values)
        std_deviations.append(std_deviation)

    return best_fitness_values, std_deviations

fitness_values, std_deviations = evolutionary_algorithm()

# Generowanie wykresu
generations = range(len(fitness_values))
plt.plot(generations, fitness_values, label='Fitness')
plt.plot(generations, std_deviations, label='Odchylenie standardowe')
plt.xlabel('Generacja')
plt.ylabel('Wartość')
plt.title('Optymalizacja funkcji jednowymiarowej ' + r'$\sin(0.5x) + \cos(0.75x)$')
plt.legend()
plt.show()
