import random
from deap import base, creator, tools
from datetime import datetime

# Global variables
chromosome_lenght = 8
number_of_genes = 5
INITIAL_POPULATION = 3000
NUM_OF_GENERATIONS = 200
CROSSOVER_PROBABILITY = 0.5
MUTATION_PROBABILITY = 0.2


# restricted_positions = {
#     1: [2, 3, 4],
#     2: [0, 7],
#     3: [3, 4, 5, 6],
#     4: [0, 1, 2, 3, 4, 5, 6, 7],
#     5: [0, 1, 2, 3]
# }

restricted_positions = {
    1: [0, 1, 2, 3, 4, 5, 6, 7],
    2: [0, 1, 2, 3, 4, 5, 6, 7],
    3: [0, 1, 2, 3, 4, 5, 6, 7],
    4: [0, 1, 2, 3, 4, 5, 6, 7],
    5: [0, 1, 2]
}

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox = base.Toolbox()

# Attribute generator: generates numbers from 0 to 5 for each gene in the chromosome
toolbox.register("attr_int", random.randint, 0, number_of_genes)
# Structure initializer: creates an individual consisting of 120 such genes
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, chromosome_lenght)
# Population initializer
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def evaluate(individual):
    current_score = 0
    total_score = 0
    prev_value = None
    penalty = 0  # Initialize penalty for placing numbers in restricted positions

    for index, value in enumerate(individual):
        # Check if the current value is placed in a restricted position
        if index in restricted_positions.get(value, []):
            penalty += 2  # Increase penalty for restricted placement

        # Check if the block is left empty and apply penalty
        if value == 0:
            penalty += 1

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

    # Adjust the total score by the penalty. Ensure the final score is not negative
    final_score = max(0, total_score - penalty)

    return (final_score,)


# Register the evaluation function
toolbox.register("evaluate", evaluate)

# Register genetic operators
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxOnePoint)  # For one-point crossover
toolbox.register("mate", tools.cxTwoPoint)  # For two-point crossover
toolbox.register("mate", tools.cxUniform, indpb=0.1)  # For uniform crossover, with a swapping probability of 10%

toolbox.register("mutate", tools.mutUniformInt, low=1, up=5, indpb=0.05)


def run_genetic_algorithm(include_individuals=None, initial_population=INITIAL_POPULATION, num_of_generations=NUM_OF_GENERATIONS):
    if include_individuals:
        # Reduce the number of new individuals to generate
        new_individuals_count = initial_population - len(include_individuals)
        population = toolbox.population(n=new_individuals_count)
        # Prepend or append top individuals from the previous run
        population.extend(include_individuals)
    else:
        population = toolbox.population(n=initial_population)

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

    # After the GA run, select and print the best individuals
    # best_individuals = tools.selBest(population, k=1)

    # Select and return the top 5 individuals
    return tools.selBest(population, k=5)

def interactive_ga_run():
    top_individuals = None
    while True:
        start_ts = datetime.now()
        print(f"Start: {start_ts}")
        if top_individuals:
            print("Rerunning GA with top individuals from previous run...")
        else:
            print("Running GA for the first time...")

        top_individuals = run_genetic_algorithm(include_individuals=top_individuals)
        end_ts = datetime.now()
        print(f"End: {end_ts}")

        time_diff = end_ts - start_ts
        print(f"Total time: {time_diff}")

        # Display the top individuals
        print("Top individuals from the current run:")
        for i, individual in enumerate(top_individuals, start=1):
            print(f"Best Individual {i}: {individual}, Fitness: {individual.fitness.values[0]}")

        # Ask the user if they want to rerun
        rerun = input("Do you want to rerun the GA with these top individuals? (yes/no): ").lower()
        if rerun != "yes":
            print("GA run complete. Final top individuals shown above.")
            break

#Example genetic algorithm loop
def main():
    interactive_ga_run()

if __name__ == "__main__":
    main()




