import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from math import sqrt, exp
def normal(x,mu=0,sigma=1):
    return 1/(sigma*sqrt(2 * math.pi)) * exp(-1/2*((x-mu)/sigma)**2)


mu = -1
sigma = 3

sample_size = [1000, 10000, 100000]

for n in sample_size:
    Z = np.random.normal(mu,sigma,n)
    plt.figure()
    plt.hist(Z,density=True, bins=int(n**0.5));

    X = np.linspace(-10,10,num=500)
    Y = [normal(x,mu,sigma) for x in X]
    plt.plot(X,Y,color='r')
