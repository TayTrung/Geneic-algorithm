import random
from pprint import pprint


def get_fittest_point(population):

    max_points = -1
    for x in range(len(population)):
        if max_points < population[x][1]:
            max_points = population[x][1]
    return max_points


def intit_population(population, population_number, gene_length, highest_point):
    for _ in range(population_number):
        gene_seq = []
        for __ in range(gene_length):
            gene_seq.append(random.randint(0, highest_point))
        population.append([gene_seq])


def cal_fittess(population):
    gene_range = len(population[0][0])
    population_length = len(population)
    for index in range(population_length):
        count = 0
        for ind in range(gene_range):
            count += population[index][0][ind]
        if len(population[index]) < 2:
            population[index].append(count)
        else:
            population[index][1] = count


def selection(population):
    first_index = -1
    second_index = -1
    population_length = len(population)
    for arr in range(population_length):
        if first_index == -1:
            first_index = arr
        elif second_index == -1:
            if population[arr][1] > population[first_index][1]:
                second_index = first_index
                first_index = arr
            else:
                second_index = arr
        elif population[arr][1] > population[first_index][1]:
            second_index = first_index
            first_index = arr
        elif population[arr][1] > population[second_index][1]:
            second_index = arr
    return [first_index, second_index]


def crossover(population, first_fittest_item, second_fittest_item):
    rand = random.randint(1, len(population[0][0]) - 1)
    print('----------- Crossover point -----------')
    print(rand)
    for index in range(rand):
        temp = first_fittest_item[index]
        first_fittest_item[index] = second_fittest_item[index]
        second_fittest_item[index] = temp


def calculate_fittes(arr):
    count = 0
    for x in range(len(arr)):
        count += arr[x]
    return count


def get_least_fittest_index(population):
    minFitVal = 99999999999999999
    minFitIndex = 0
    for x in range(len(population)):
        if minFitVal >= population[x][1]:
            minFitVal = population[x][1]
            minFitIndex = x
    return minFitIndex


def add_new_fittest_to_population_after_crossover(population, first_fittest_item, second_fittest_item):
    min_fittess_index = get_least_fittest_index(population)
    print('------------ Index of min fit ------------')
    print(min_fittess_index)
    first = first_fittest_item
    second = second_fittest_item
    first_fitt = calculate_fittes(first)
    second_fitt = calculate_fittes(second)
    if first_fitt > second_fitt:
        population[min_fittess_index] = [first, first_fitt]
    else:
        population[min_fittess_index] = [second, second_fitt]


def mutation(first_fittest_item, gene_length, highest_point):
    random_cell = random.randint(0, gene_length - 1)
    random_point = random.randint(0, highest_point)
    while random_point == first_fittest_item[0][random_cell]:
        random_point = random.randint(0, highest_point)
    first_fittest_item[0][random_cell] = random_point
    fittes = calculate_fittes(first_fittest_item[0])
    first_fittest_item[1] = fittes


def main():
    # -------------------------------------------------------------------

    # population = [[[0, 0, 0, 1, 0]],
    #               [[1, 1, 1, 1, 1]],
    #               [[0, 0, 1, 1, 0]],
    #               [[0, 1, 1, 0, 1]],
    #               [[1, 0, 1, 0, 1]]]
    population = []
    generation_count = 1
    first_fittest_item = []
    second_fittest_item = []

    highest_point = 1
    population_number = 5
    gene_length = 5
    max_generation = 5
    intit_population(population, population_number, gene_length, highest_point)
    print("------------- Init population -------------")
    pprint(population)
    cal_fittess(population)
    print("------------- Cal fittess -------------")
    pprint(population)
    fittest_point_in_population = get_fittest_point(population)
    print(
        "Generation {}: {} points out of {}".format(generation_count, fittest_point_in_population, gene_length*highest_point))

    while fittest_point_in_population < (highest_point * gene_length) and generation_count < max_generation:
        # while generation_count < max_generation:

        generation_count += 1
        index = selection(population)
        print("------------- Get 1st and 2nd fittest index -------------")
        print(index)
        first_fittest_item = population[index[0]][0][:]
        second_fittest_item = population[index[1]][0][:]
        print("------------- First fittest -------------")
        print(first_fittest_item)
        print("------------- Second fittest -------------")
        print(second_fittest_item)
        crossover(population, first_fittest_item, second_fittest_item)
        print("------------- First fittest after crossover -------------")
        print(first_fittest_item)
        print("------------- Second fittest after crossover -------------")
        print(second_fittest_item)
        #  20% that Mutation will happen
        if random.randint(1, 10) > 8:
            print('------------- Mutation of first fittest item ------------')
            mutation(population[index[0]], gene_length, highest_point)
            pprint(population)

        add_new_fittest_to_population_after_crossover(
            population, first_fittest_item, second_fittest_item)
        print('--------- Current population -------------')
        pprint(population)
        fittest_point_in_population = get_fittest_point(population)

        print(
            "Generation {}: {} points out of {}".format(generation_count, fittest_point_in_population, (gene_length*highest_point)))
    if fittest_point_in_population == (gene_length*highest_point):
        print("Solution found in generation {}!".format(generation_count))
        print("Fitness: {} out of {}!".format(
            fittest_point_in_population, (gene_length*highest_point)))
    else:
        print("Solution not found!")
        print("Reached maxium allowed generation:  {} generations!".format(
            generation_count))
        print("Fitness: {} out of {}!".format(
            fittest_point_in_population, (gene_length*highest_point)))


main()
