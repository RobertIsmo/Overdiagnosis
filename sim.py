import random

population = 100000
afliction_rate = .5
screening_rate = .5


#trivial
lethality_rate = .5
treated_lethality_rate = .05
treatment_rate = .2

"""
    death is assumed to be death by the disease
    when lethality is up inflation goes down and overdiagnosis goes down
    when treated lethality goes up the inflation increases
    when treatment rate goes up overdiagnosis increases
    
"""

def simulate(pop, rate):
    count = 0
    for _ in range(pop):
        if(random.random() < rate):
            count += 1
    return count
def run(times):
    te = 0
    od = 0
    for _ in range(times):
        #the amount of the population that is positive
        aflicted_population = simulate(population, afliction_rate)
        #the amount positively screened
        diagnosed = simulate(aflicted_population, screening_rate)
        # of the diagnosed untreated population, the amount lethal
        deaths = simulate(aflicted_population, lethality_rate)

        #the amount positively diagnosed who are given treatment
        treated = simulate(diagnosed, treatment_rate)

        #the amount positively diagnosed who would not have died
        unlethal_diagnosed = simulate(treated, 1-lethality_rate)
        #the amount positively diagnosed, given the treatment, who would not have died
        overdiagnosed = simulate(unlethal_diagnosed, treatment_rate)

        overdiagnosed_rate = overdiagnosed/treated

        #the amount positively diagnosed who are not given treatment
        diagnosed_untreated = simulate(diagnosed, 1-treatment_rate)
        #the amount positively diagnosed, not given treatment, who die
        dead_untreated = simulate(diagnosed_untreated, lethality_rate)

        lethal_untreated_rate = dead_untreated/diagnosed_untreated

        #the performance of the treatment, the amount who will be unaffected by the disease
        treatment_efficacy = 1 - (treated_lethality_rate/lethal_untreated_rate)
        cured = simulate(treated, treatment_efficacy)
        te += treatment_efficacy
        od += overdiagnosed_rate
    return [te/times,od/times]

results = run(30)
print("<===this is the test for the values of===>")
print("lethality rate: {}".format(lethality_rate))
print("lethality rate(for treated individuals): {}".format(treated_lethality_rate))
print("population positivity: {}".format(afliction_rate))
print("the rate at which the population is screened: {}".format(screening_rate))
print("the rate of people given treatment: {}".format(treatment_rate))
print('\n')
print((1-treated_lethality_rate)-results[0])
print(results[1])

