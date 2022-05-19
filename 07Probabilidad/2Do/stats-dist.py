
from scipy.stats import binom

for i in range(9):
    rnd_binom = binom.rvs(n = 12, p = 0.6)
    print(rnd_binom)