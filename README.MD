links:

https://www.cancercenter.com/become-a-patient/our-treatment-results/survival-statistics-and-results/statistical-methodology

https://www.sciencedirect.com/science/article/pii/S2001037014000464

https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-019-0801-4

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5402773/

https://seer.cancer.gov/data/product-comparison.html

https://www.facs.org/quality-programs/cancer/ncdb/publicaccess

https://www.facs.org/-/media/files/quality-programs/cancer/ncdb/ncdb_tools_2021.ashx


Input parameters considered:

population = 100000       #Number of people in the population
afliction_rate = .2       #Percent of people that have the disease (20%)
screening_rate = .75      #Percent of people that are screened for the disease (75%)

untreated_death_rate = .4 #Percent of people that die without treatment (40%)
treated_death_rate = .1   #Percent of people that die with treatment (10%)
treatment_rate = .9       #Percent of people electing to have treatment (90%)


Output parameters:

overdiagnosis_rate = .539 #Percent of the treated population that was overdiagnosed
treatment_efficacy = .752 #How effective the treatment is at reducing deaths: 1 - (treated_death_rate/untreated_death_rate)


Relationships considered between the parameters:

aflicted_population = population * afliction_rate
diagnosed_population = aflicted_population * screening_rate
untreated_deaths = aflicted_population * untreated_death_rate
treated_population = diagnosed_population * treatment_rate
unlethal_diagnosed_population = treated_population * (1-untreated_death_rate)
overdiagnosed_population = unlethal_diagnosed_population * treatment_rate
overdiagnosis_rate = overdiagnosed_population/treated_population
diagnosed_untreated_population = diagnosed_population * (1-treatment_rate)
diagnosed_untreated_deaths = diagnosed_untreated_population * untreated_death_rate
diagnosed_untreated_death_rate = diagnosed_untreated_deaths/diagnosed_untreated_population
treatment_efficacy = 1 - (treated_death_rate/diagnosed_untreated_death_rate)


General Assumption:

untreated_death_rate = 0.4


Main Findings:

screening_rate has no effect on results
when untreated_death_rate increases, overdiagnosis rate decreases and treatment efficacy increases 
when untreated_death_rate decreases, overdiagnosis rate increases and treatment efficacy decreases
when treatment_rate increases, overdiagnosis rate increases
when treatment_rate decreases, overdiagnosis rate decreases
