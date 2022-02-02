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

#Parameters
#*Note: These numbers are for testing purposes, we still need the actual data
population = 100000       #Number of people in the population
afliction_rate = .2       #Percent of people that have the disease (20%)
screening_rate = .75      #Percent of people that are screened for the disease (75%)

untreated_death_rate = .4 #Percent of people that die without treatment (40%)
treated_death_rate = .1   #Percent of people that die with treatment (10%)
treatment_rate = .9       #Percent of people electing to have treatment (90%)

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

def run(trials) -> list:
    '''Function to run experiment for an amount of trials'''
    overdiagnosis_rate_count = 0
    treatment_efficacy_count = 0
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
        overdiagnosed_rate = overdiagnosed_population/treated_population

        #The population that is diagnosed and not given treatment
        diagnosed_untreated_population = simulate(diagnosed_population, 1-treatment_rate)
        #The population diagnosed, not given treatment, and die
        diagnosed_untreated_deaths = simulate(diagnosed_untreated_population, untreated_death_rate)

        diagnosed_untreated_death_rate = diagnosed_untreated_deaths/diagnosed_untreated_population

        #The performance of the treatment
        treatment_efficacy = 1 - (treated_death_rate/diagnosed_untreated_death_rate)

        #The population that is cured of the disease
        cured_population = simulate(treated_population, treatment_efficacy)

        overdiagnosis_rate_count += overdiagnosed_rate
        treatment_efficacy_count += treatment_efficacy
    return [overdiagnosis_rate_count/trials, treatment_efficacy_count/trials]

#Main
results = run(30)
print("<===Test for the following values===>")
print("Untreated Death rate: {}".format(untreated_death_rate))
print("Treated Death rate: {}".format(treated_death_rate))
print("Affliction Rate: {}".format(afliction_rate))
print("Screening Rate: {}".format(screening_rate))
print("Treatment Rate: {}".format(treatment_rate))
print('---------------\n\nResults:')
print("Overdiagnosis Rate: {}".format(results[0]))
print("Treatment Efficacy: {}".format(results[1]))