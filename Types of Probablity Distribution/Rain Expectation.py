import scipy.stats as stats

prob1 = stats.poisson.pmf(6, 10)
print("Probablity of raining for exactly 6 days is:", prob1)

prob2 = stats.poisson.pmf(12, 10) + stats.poisson.pmf(13, 10) + stats.poisson.pmf(14, 10)
print("Probablity of raining for 12, 13 or 14 days is:", prob2)