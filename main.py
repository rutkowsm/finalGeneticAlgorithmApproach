import random
from deap import base, creator, tools

# Global variables
CHROMOSOME_LENGHT = 130
INITIAL_POPULATION = 1000
NUM_OF_GENERATIONS = 100
CROSSOVER_PROBABILITY = 0.5
MUTATION_PROBABILITY = 0.2

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox = base.Toolbox()

# Attribute generator: generates numbers from 0 to 5 for each gene in the chromosome
toolbox.register("attr_int", random.randint, 1, 5)
# Structure initializer: creates an individual consisting of 120 such genes
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, CHROMOSOME_LENGHT)
# Population initializer
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# population = toolbox.population(n=50)  # Example: create a population of 50 individuals
#
# best_individuals = tools.selBest(population, k=5)

# Define the evaluation function
def evaluate(individual):
    current_score = 0
    total_score = 0
    prev_value = None

    for value in individual:
        if value == prev_value:
            # If the current value is the same as the previous, increment the score
            current_score += 1
        else:
            # Add the current_score to total_score whenever a sequence ends
            total_score += current_score
            current_score = 0  # Reset score for the new value
        prev_value = value

    # Add the last sequence score to total_score
    total_score += current_score

    return (total_score,)


# Register the evaluation function
toolbox.register("evaluate", evaluate)

# Register genetic operators
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxOnePoint)  # For one-point crossover
toolbox.register("mate", tools.cxTwoPoint)  # For two-point crossover
toolbox.register("mate", tools.cxUniform, indpb=0.1)  # For uniform crossover, with a swapping probability of 10%

toolbox.register("mutate", tools.mutUniformInt, low=0, up=5, indpb=0.05)

# Example genetic algorithm loop
def main():
    population = toolbox.population(n=INITIAL_POPULATION)  # Initialize population

    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit

    for g in range(NUM_OF_GENERATIONS):
        # Select the next generation individuals
        offspring = toolbox.select(population, len(population))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CROSSOVER_PROBABILITY:  # Check if we should perform crossover
                toolbox.mate(child1, child2)  # Apply the registered crossover operation
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTATION_PROBABILITY:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        population[:] = offspring

    # After the GA run, select and print the 5 best individuals
    best_individuals = tools.selBest(population, k=5)
    for i, individual in enumerate(best_individuals, start=1):
        print(f"Best Individual {i}: {individual}, Fitness: {individual.fitness.values[0]}")

if __name__ == "__main__":
    main()




