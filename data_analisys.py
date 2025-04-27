import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
def uniform_density(x, a=0, b=1):
    if a <= x <= b:
        return 1/(b-a)
    else:
        return 0

def normal_density(x, mu=0, sigma=1):
    return 1/(sigma*math.sqrt(2 * math.pi)) * math.exp(-1/2*((x-mu)/sigma)**2)

def exponential_density(x, lambd=1):
    if x > 0:
        return lambd*math.exp(-lambd*x)
    else:
        return 0

def plot_hist_info(D):
    print(list(D)[:20]) # Печатаем первые 20 значений
    plt.hist(D, density=True , bins=int(len(D)**0.5)); # Строим гистограмму
    print('Математическое ожидание:', np.mean(D))
    print('Стандартное отклонение:', np.std(D))

def plot_hist_funct(D, fun):
    plt.hist(D, density=True, bins=int(len(D)**0.5)); # Строим гистограмму

    X = np.linspace(min(D)-1,max(D)+1, num=200)
    Y = [fun(x) for x in X]
    plt.plot(X,Y) # Рисуем график функции
