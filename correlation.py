
'''
Реализуйте функцию corr(X,Y), которая находит коэффициент корреляции между выборками X и Y
Заметим, что для поиска среднего значения  A¯¯¯¯  выборки  A  есть функция A.mean(), для посика стандартного отклонения выборки  σ(А)  есть функция А.std().
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
def corr(X,Y):
    n = len(X)
    X_m = X.mean()
    Y_m = Y.mean()
    count1 = 0
    for i in range(1,n):
      count1 += (X[i] - X_m) * (Y[i] - Y_m)
    core = (count1 / n)/(X.std() * Y.std())

    return core

X = np.array([1,2,3,4])
Y = np.array([1,2,3,4])
print(corr(X,Y)) ## Ответ должен быть 1


X = np.array([1,2,3,4])
Y = np.array([2,4,6,8])
print(corr(X,Y)) ## Ответ должен быть 1


X = np.array([1,2,3,4])
Y = np.array([-2,-4,-6,-8])
print(corr(X,Y)) ## Ответ должен быть -1

X = np.array([-1,1,-1,1])
Y = np.array([1,1,-1,-1])
print(corr(X,Y)) ## Ответ должен быть 0
