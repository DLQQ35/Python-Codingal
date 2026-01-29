import scipy.stats as stats

prob1 = stats.poisson.cdf(12, 10)
print("Probablity of raining for exactly 12 days is:", prob1)

prob2 = stats.poisson.cdf(18, 10) - stats.poisson.cdf(11, 10)
print("Probablity of raining for 12-18 days is:", prob2)