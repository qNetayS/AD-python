import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from math import sqrt, exp
mu = 5
sigma = 10
n = 1000
X = np.random.normal(mu, sigma, n)
print(sum(X>sigma) / n)
print(sum(X>2*sigma) / n)
print(sum(X>3*sigma) / n)
