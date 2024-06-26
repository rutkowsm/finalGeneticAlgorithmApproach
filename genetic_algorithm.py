import random
from deap import base, creator, tools
from datetime import datetime
import data as d
import calendar_processing as cp
from copy import deepcopy

# Global variables
INITIAL_POPULATION = 2000
NUM_OF_GENERATIONS = 200
CROSSOVER_PROBABILITY = 0.5
MUTATION_PROBABILITY = 0.2

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox = base.Toolbox()


def evaluate(individual, restricted_positions=None):
    if restricted_positions is None:
        restricted_positions = {}
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
    final_score = max(-10, total_score - penalty)

    return (final_score,)


# Register the evaluation function
toolbox.register("evaluate", evaluate)

# Register genetic operators
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxOnePoint)  # For one-point crossover
toolbox.register("mate", tools.cxTwoPoint)  # For two-point crossover
toolbox.register("mate", tools.cxUniform, indpb=0.1)  # For uniform crossover, with a swapping probability of 10%

toolbox.register("mutate", tools.mutUniformInt, low=1, up=5, indpb=0.05)


def run_genetic_algorithm(chromosome_lenght=None, gene_count=None, restricted_positions=None, include_individuals=None,
                          initial_population=INITIAL_POPULATION,
                          num_of_generations=NUM_OF_GENERATIONS):
    # Attribute generator: generates numbers from 0 to gene_count for each gene in the chromosome
    toolbox.register("attr_int", random.randint, 0, gene_count)
    # Structure initializer: creates an individual consisting of 120 such genes
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, chromosome_lenght)
    # Population initializer
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    if restricted_positions is None:
        restricted_positions = []

    if include_individuals:
        # Reduce the number of new individuals to generate
        new_individuals_count = initial_population - len(include_individuals)
        population = toolbox.population(n=new_individuals_count)
        # Prepend or append top individuals from the previous run
        population.extend(include_individuals)
    else:
        population = toolbox.population(n=initial_population)

        # Evaluate the entire population with restricted_positions
        fitnesses = list(map(lambda ind: toolbox.evaluate(ind, restricted_positions), population))
        for ind, fit in zip(population, fitnesses):
            ind.fitness.values = fit

    for g in range(num_of_generations):
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
        fitnesses = map(lambda ind: toolbox.evaluate(ind, restricted_positions), invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        population[:] = offspring

    # After the GA run, select and print the best individuals
    # best_individuals = tools.selBest(population, k=1)

    # Select and return the top 5 individuals
    return tools.selBest(population, k=1)


def interactive_ga_run(chromosome_lenght, gene_count, unavailabilities):
    top_individuals = None
    while True:
        # start_ts = datetime.now()
        # print(f"Start: {start_ts}")
        # if top_individuals:
        #     print("Rerunning GA with top individuals from previous run...")
        # else:
        #     print("Running GA for the first time...")

        top_individuals = run_genetic_algorithm(restricted_positions=unavailabilities,
                                                include_individuals=top_individuals,
                                                chromosome_lenght=chromosome_lenght, gene_count=gene_count)
        # end_ts = datetime.now()
        # print(f"End: {end_ts}")
        #
        # time_diff = end_ts - start_ts
        # print(f"Total time: {time_diff}")

        # Display the top individuals
        # print("Top individuals from the current run:")
        for i, individual in enumerate(top_individuals, start=1):
            print(f"Best Individual {i}: {individual}, Fitness: {individual.fitness.values[0]}")

        # Ask the user if they want to rerun
        rerun = 'no'  # input("Do you want to rerun the GA with these top individuals? (yes/no): ").lower()
        if rerun != "yes":
            # print("GA run complete. Final top individuals shown above.")
            break

    return top_individuals


def run_ga_iterations(schedule, employees):
    """
    Add your function description here.
    """
    start_ts = datetime.now()
    print(f"Start: {start_ts}")

    schedule_copy = deepcopy(schedule)  # Copy to avoid mutating the original schedule

    cp.print_full_schedule(schedule_copy)

    for date, shifts in schedule_copy.items():
        for shift_num, shift_hours in shifts.items():
            # Process current shift unavailabilities
            shift_details = cp.process_shift_unavailabilities(employees, date, shift_num, list(shift_hours.keys()))
            shift_len = shift_details["shift_len"]
            unavailabilities = shift_details["unavailabilities"]
            print('   ')
            print(f"NEW SHIFT: '{date}' Shift {shift_num}: length: {shift_len}")
            print(f"Unavailabilities: {unavailabilities}")

            # Run the genetic algorithm for the shift
            best_individual = interactive_ga_run(chromosome_lenght=shift_len, gene_count=len(employees),
                                                 unavailabilities=unavailabilities)
            if best_individual is None:
                print(f"No best individual found for shift {shift_num} on {date}.")
                continue  # Skip to the next shift if no best individual was found

            # Update employee calendars based on GA results
            # More flexible: Flatten the list if it's a list of lists, otherwise leave it as is
            employee_indexes = [item for sublist in best_individual for item in sublist] if any(
                isinstance(el, list) for el in best_individual) else best_individual

            cp.update_employee_calendar(date=date, shift_hours=list(shift_hours.keys()),
                                        best_individual=employee_indexes, employees=employees)
            # Assuming the variables date, shift_num, best_individual, employees, and schedule_copy are defined and available
            cp.update_schedule_with_names(date=date, shift_num=shift_num, best_individual=employee_indexes,
                                          employees=employees, schedule=schedule_copy)

            print(f"Shift hours: {shift_hours}")
            print("    ")

            cp.print_employee_calendars(employees)

    cp.print_full_schedule(schedule_copy)

    end_ts = datetime.now()
    print(f"End: {end_ts}")

    time_diff = end_ts - start_ts
    print(f"Total time: {time_diff}")


current_employees = cp.process_employees(d.employees)
current_schedule = d.schedule

run_ga_iterations(schedule=current_schedule, employees=current_employees)

# def main():
#     positions = {
#         1: [2, 3, 4],
#         2: [0, 7, 8, 9],
#         3: [3, 4, 5, 6],
#         4: [0, 1, 2, 3, 4, 5, 6, 7],
#         5: []
#     }
#     chromosome_lenght = 8
#     gene_count=5
#     interactive_ga_run(chromosome_lenght=chromosome_lenght, gene_count=gene_count, unavailabilities=positions)
#
#
# if __name__ == "__main__":
#     main()
