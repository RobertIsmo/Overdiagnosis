from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1,1)
mean, var, skew, kurt = stats.norm.stats(moments='mvsk')

x = np.linspace(stats.norm.ppf(0.01), stats.norm.ppf(0.99), 100)
ax.plot(x, stats.norm.pdf(x), 'r-', lw=1, alpha=0.6, label='norm')

plt.show()
