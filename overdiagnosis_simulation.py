''' Overdiagnosis Simulation by William Brown and Robert Ismo 

This file uses the parameters described below to simulate the overdiagnosis rate and treatment efficacy for a disease.
------------------------------------------
NOTES:
death is assumed to be death by the disease
data such as untreated_death_rate may be hard to find
------------------------------------------
FINDINGS:
population has no effect on results
afliction_rate has no effect on results
screening_rate has no effect on results
when untreated_death_rate increases, overdiagnosis rate decreases and treatment efficacy increases 
when untreated_death_rate decreases, overdiagnosis rate increases and treatment efficacy decreases
treated_death_rate has no effect on overdiagnosis rate
when treated_death_rate increases, treatment efficacy decreases
when treated_death_rate decreases, treatment efficacy increases
when treatment_rate increases, overdiagnosis rate increases
when treatment_rate decreases, overdiagnosis rate decreases
treatment_rate has no effect on treatment efficacy
'''

#Imports
import random
import matplotlib.pyplot as plt

#Parameters
#*Note: These numbers are for testing purposes, we still need the actual data
population = 100000       #Number of people in the population
afliction_rate = .2       #Percent of people that have the disease (20%)
screening_rate = .75     #Percent of people that are screened for the disease (75%)

untreated_death_rate = .4 #Percent of people that die without treatment (40%)
treated_death_rate = .1   #Percent of people that die with treatment (10%)
treatment_rate = .9       #Percent of people electing to have treatment (90%)

test_parameter = 'none'

#Functions
def simulate(pop, rate) -> int:
    '''Function to simulate with some randomness
    *Note: we can replace this with the standard deviation to account for randomness
    '''
    count = 0
    for _ in range(pop):
        if(random.random() < rate):
            count += 1
    return count

def run(trials, test_parameter) -> list:
    '''Function to run experiment for an amount of trials'''
    #screening_rate = 0
    global screening_rate
    global untreated_death_rate
    global treatment_rate
    overdiagnosis_rate_count = 0
    treatment_efficacy_count = 0
    overdiagnosis_list = []
    test_parameter_list = []
    for _ in range(trials):
        #The population that has the disease
        aflicted_population = simulate(population, afliction_rate)
        #The population that is screened positive for the disease
        diagnosed_population = simulate(aflicted_population, screening_rate)
        #The population that does not have treatment and dies
        untreated_deaths = simulate(aflicted_population, untreated_death_rate)

        #The population that is diagnosed and given treatment
        treated_population = simulate(diagnosed_population, treatment_rate)

        #The population that is diagnosed who would not have died without treatment
        unlethal_diagnosed_population = simulate(treated_population, 1-untreated_death_rate)

        #The population that is diagnosed, given the treatment, who would not have died
        overdiagnosed_population = simulate(unlethal_diagnosed_population, treatment_rate)

        #***The overdiagnosis rate***
        overdiagnosis_rate = overdiagnosed_population/treated_population

        #The population that is diagnosed and not given treatment
        diagnosed_untreated_population = simulate(diagnosed_population, 1-treatment_rate)
        #The population diagnosed, not given treatment, and die
        diagnosed_untreated_deaths = simulate(diagnosed_untreated_population, untreated_death_rate)

        if diagnosed_untreated_population != 0:
            diagnosed_untreated_death_rate = diagnosed_untreated_deaths/diagnosed_untreated_population
        else:
            diagnosed_untreated_death_rate = 0

        #The performance of the treatment
        if diagnosed_untreated_death_rate != 0:
            treatment_efficacy = 1 - (treated_death_rate/diagnosed_untreated_death_rate)
        else:
            treatment_efficacy = 0

        #The population that is cured of the disease
        cured_population = simulate(treated_population, treatment_efficacy)

        overdiagnosis_rate_count += overdiagnosis_rate
        treatment_efficacy_count += treatment_efficacy

        overdiagnosis_list.append(overdiagnosis_rate)

        if test_parameter == 'screening_rate':
            test_parameter_list.append(screening_rate)
            screening_rate += 0.1
        elif test_parameter == 'untreated_death_rate':
            test_parameter_list.append(untreated_death_rate)
            untreated_death_rate += 0.1
        elif test_parameter == 'treatment_rate':
            test_parameter_list.append(treatment_rate)
            treatment_rate += 0.1
            
    if test_parameter != 'none':
        plot(test_parameter_list, overdiagnosis_list, test_parameter)

    return [overdiagnosis_rate_count/trials, treatment_efficacy_count/trials]

def plot(xAxis, yAxis, parameter):
    plt.plot(xAxis,yAxis)
    plt.title('{} vs overdiagnosis_rate'.format(parameter))
    plt.xlabel(parameter)
    plt.ylabel('overdiagnosis_rate')
    plt.show()

#Main
results = run(10, test_parameter)
print("<===Test for the following values===>")
print("Population: {}".format(population))
print("Untreated Death rate: {}".format(untreated_death_rate))
print("Treated Death rate: {}".format(treated_death_rate))
print("Affliction Rate: {}".format(afliction_rate))
print("Screening Rate: {}".format(screening_rate))
print("Treatment Rate: {}".format(treatment_rate))
print('---------------\n\nResults:')
print("Overdiagnosis Rate: {}".format(results[0]))
print("Treatment Efficacy: {}".format(results[1]))