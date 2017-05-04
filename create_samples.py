import re
import random
import matplotlib.pyplot as plt
#from matplotlib.gridspec import subplot2grid
#from matplotlib.gridspec import GridSpec
#import matplotlib.patches as patches

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


pop_resp = 0.0
pop_total = 0.0
sample_size = 300 #default size is 300
number_samples = 25.0 #default number is 25

def get_numbers():
    total = float(input('Enter total population size: '))
    resp = float(input('Enter responsive (sub)population size: '))
    size = int(input('Enter the sample size: '))
    number = float(input('Enter the number of samples: '))
    return total, resp, size, number

def run_samples():
    [pop_total, pop_resp, sample_size, number_samples] = get_numbers()
    population = create_population(pop_resp,(pop_total-pop_resp))
    prevalence = float(pop_resp/pop_total)
    print('actual prevalence: {:.2f}'.format(prevalence))
    fracs = [100.0*pop_resp/pop_total, 100.0*(pop_total-pop_resp)/pop_total]
    avg_responsiveness = 100.0*get_mean(get_many_samples(population, sample_size, number_samples))
    sample_fracs = [avg_responsiveness, 100-avg_responsiveness]

    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(121, aspect = 'equal')
    ax1 = plt.subplot2grid((2,6),(0,0), rowspan = 2, colspan = 3, aspect = 'equal')
    labels = ['R ({:.0f})'.format(pop_resp), 'NR ({:.0f})'.format(pop_total-pop_resp)]
    ax1.pie(fracs, labels=labels, colors=['red','blue'], autopct='%.0f%%')

    #ax2 = fig1.add_subplot(122, aspect = 'equal')
    ax2 = plt.subplot2grid((2,6),(0,4), aspect = 'equal')
    labels = ['R ({:.0f})'.format(avg_responsiveness*sample_size/100), 'NR ({:.0f})'.format(sample_size-(avg_responsiveness*sample_size/100))]
    ax2.pie(sample_fracs, labels=labels, colors=['red','blue'], autopct='%.0f%%')

    plt.tight_layout()

    fig1.savefig('sample_charts.png')

    
  
'''
fig1 = plt.figure()
ax1 = fig1.add_subplot(111,aspect = 'equal')
ax1.add_patch(patches.Rectangle((0.5,0.5), 1, 1))
plt.axis('equal')
plt.axis('off')
#fig1.savefig('rect1.png', dpi= 90, bbox_inches='tight')
#plt.show()
fig1.savefig('your_graph.png')
'''
'''
round_one = get_many_samples(population, sample_size, number_samples)
#print(round_one)
mean = get_mean(round_one)
difference = abs(mean - prevalence)
print('{:.3f}'.format(mean))
print('{:.3f}'.format(difference))
print(' ')
'''
'''
sample_size = 1000
number_samples = 25
round_two = get_many_samples(population, sample_size, number_samples)
print(round_two)
mean = get_mean(round_two)
difference = abs(mean - prevalence)
print(mean)
print(difference)
'''
