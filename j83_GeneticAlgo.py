# Simulation of variations in fitness of population during crossover and mutations using Genetic Algorithm
from __future__ import division
import random

generations = []
population = []
avg_fitness = []
size = []
weights = [5, 3, 4, 3, 2]
# intelligence, weight, height, complexity, hair color

class dna:
	def __init__(self):
		self.values = []
		self.fitness_score = -1

def pop_generator(sizer, population):
	for i in range(0, sizer):
		person = dna()
		valuer = []
		for j in range(0, 5):
			valuer.append(random.randint(0, 1))
		person.values = valuer
		population.append(person)
	return population

def fitness_fn(population, weights):
	fitness_sum = 0
	for person in population:
		score = 0
		for i in range(0, 5):
			if person.values[i] == 1:
				score += weights[i]
		person.fitness_score = score
		fitness_sum += score
	return fitness_sum

def crossover_gen(x, y):
	factor = random.randint(0,5)
	z = dna()
	for i in range(0, 5):
		z.values.append(0)
		if i < factor:
			z.values[i] = x.values[i]
		else:
			z.values[i] = y.values[i]
	return z

def threshold(population, sizer):
	new_gen = []
	sizer = int(sizer / 3)
	for i in range(0, sizer, 2):
		new_gen.append(crossover_gen(population[i], population[i+1]))
	return new_gen

def mutation(population, sizer, rate):
	factor = int(sizer * rate / 100)
	if factor > 1:
		for x in range(0, factor):

			mutant = random.randint(0, sizer - 2)
			muted = random.randint(0, 4)

			if population[mutant].values[muted] == 0:
				population[mutant].values[muted] = 1
			else:
				population[mutant].values[muted] = 0

	else:
		print("Mutation in population is insignificant.")

	return population


size.append(int(input("Enter the size of initial population : ")))
avg_fit_desired = int(input("Enter the desired average fitness (%) for the final population : "))
mutation_rate = int(input("Enter the mutation rate (%) in population : "))

index = 0
avg_fitness.append(0)

population = pop_generator(size[index], population)
flag = True

while flag:

	generations.append(population)
	fitness_sum = fitness_fn(population, weights)
	avg_fitness[index] = float(fitness_sum) / size[index] * 4

	population.sort(key=lambda x: x.fitness_score, reverse=True)

	# for x in population:
	# 	print(x.fitness_score)

	print("\nCurrent Generation : " + str(index))
	print("Population Size : " + str(len(population)))
	print("Average Fitness : " + str(avg_fitness[index])+" %")

	population = threshold(population, size[index])
	population = mutation(population, int(size[index] / 6), mutation_rate)

	index += 1
	avg_fitness.append(0)
	size.append(int(size[index-1]/6))
	if avg_fitness[index - 1] > avg_fit_desired:
		flag = False
		print("\nPopulation satisfies average fitness requirement at generation : " + str(index - 1))
	elif size[index] == 0:
		flag = False
		print("\nPopulation exhausted before average fitness achieved.")


