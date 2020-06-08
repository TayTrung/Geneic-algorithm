import random

population = [[[0, 0, 0, 0, 0]], [[0, 1, 1, 0, 1]], [[
    1, 0, 1, 1, 1]], [[0, 0, 0, 1, 0]], [[1, 1, 0, 0, 0]]]
fittess = []

first_fittest_item = []
second_fittest_item = []


def cal_fittess():
    for index in range(len(population)):
        print(index)
        count = 0
        for ind in range(len(population[index][0])):
            if population[index][0][ind] == 1:
                count += 1
        population[index].append(count)




def get_first_and_second_fittest():
    for item in fittess:
        if item > first_fittest_item:
            second_fittest_item = first_fittest_item
            first_fittest_item = item
        elif item > second_fittest_item:
            second_fittest_item = item


def crossover():
    rand = random.randint(1, len(population[0]) - 2)
    for index in rand:
        temp = pop
        first_fittest_item = second_fittest_item[index]
        second_fittest_item[index] = temp


# crossover()
