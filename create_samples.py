import re
import random

def add_doc_type(number, doctype):
	if re.match('non', doctype):
		responsive = 0
	else:
		responsive = 1

	temp_array = []
	i = 0
	while i < number:
		temp_array.append(responsive)
		i += 1
	return temp_array

def create_population(responsive, nonresponsive):
	temp_array = []
	for x in add_doc_type(responsive,'responsive'):
		temp_array.append(x)
	for x in add_doc_type(nonresponsive,'nonresponsive'):
		temp_array.append(x)
	return temp_array

def get_sample(pop, sample_sz):
	sample =  random.sample(pop,sample_sz)

	#returns number of responsive
	x = 0
	for number in sample:
		if number == 1:
			x += 1
	return x

def get_many_samples(pop,sample_sz, num_samples):
	temp_array = []
	x = 0
	while x < num_samples:
		a = get_sample(pop,sample_sz)
		temp_array.append(1.0*a/sample_sz)
		x += 1
	return temp_array

def get_mean(a_list):
	mean = sum(a_list)/len(a_list)
	return mean

#def get_RMS():
#def get_STD():

pop_resp = 30000.0
pop_total = 130000.0
sample_size = 100
number_samples = 25.0

population = create_population(pop_resp,(pop_total-pop_resp))
prevalence = float(pop_resp/pop_total)
print('actual prevalence: {:f}'.format(prevalence))



round_one = get_many_samples(population, sample_size, number_samples)
print(round_one)
mean = get_mean(round_one)
difference = abs(mean - prevalence)
print(mean)
print(difference)
print(' ')

sample_size = 1000
number_samples = 25
round_two = get_many_samples(population, sample_size, number_samples)
print(round_two)
mean = get_mean(round_two)
difference = abs(mean - prevalence)
print(mean)
print(difference)

