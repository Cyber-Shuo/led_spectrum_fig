import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.collections import LineCollection
from PIL import Image
import numpy as np
from pathlib import Path
import re
import string
from scipy.stats import norm
from scipy.optimize import curve_fit
from astropy.modeling import models, fitting

def GaussFunc(x, counts, mu, sigma):
    return counts*np.exp(-((x-mu)/np.sqrt(2)/sigma)**2)

def getdata(path,a,A,total_A,mean_A):
    with open(path,'r') as f:
        lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        a.append(value[0])
        A.append(value[1])

    MAX_A = a[A.index(max(A))]
    print('MAX =', MAX_A)

    for i in range(0, len(A)):
        total_A = total_A + A[i]

    for j in range(0, len(A)):
        mean_A = mean_A + A[j]
        if mean_A <= total_A/2:
            continue
        else:
            mean_A = a[j]
            print('mean_A =', mean_A)
            break

def gauss_fit(a, A, fit_A_list):
    popt, pcov = curve_fit(GaussFunc, a, A, bounds =([100,400,0],[100000,500,100]))
    print(popt)
    for i in a:
        fit_A = GaussFunc(i, *popt)
        fit_A_list.append(fit_A)
    return fit_A_list

fig, ax = plt.subplots()

path_a = Path("your path")
a, A, total_A, mean_A, fit_A_list  = [],[],0,0,[]
getdata(path_a, a, A, total_A, mean_A)
gauss_fit(a, A, fit_A_list)
ax.plot(a, fit_A_list, color = 'r', label = 'file name')
ax.plot(a, A, '.', markersize = 0.3, color = 'black', label = 'file name')

path_b = Path("your path")
b, B, total_B, mean_B, fit_B_list  = [],[],0,0,[]
getdata(path_b, b, B, total_B, mean_B)
gauss_fit(b, B, fit_B_list)
ax.plot(b, fit_B_list, color = 'g', label = 'file name')
ax.plot(b, B, 'x', markersize = 0.3, color = 'black', label = 'file name')

path_c = Path("your path")
c, C, total_C, mean_C, fit_C_list  = [],[],0,0,[]
getdata(path_c, c, C, total_C, mean_C)
gauss_fit(c, C, fit_C_list)
ax.plot(c, fit_C_list, color = 'b', label = 'file name')
ax.plot(c, C, '--', markersize = 0.3, color = 'black', label = 'file name')

path_d = Path("your path")
d, D, total_D, mean_D, fit_D_list  = [],[],0,0,[]
getdata(path_d, d, D, total_D, mean_D)
gauss_fit(d, D, fit_D_list)
ax.plot(d, fit_D_list, color = 'y', label = 'file name')
ax.plot(d, D, 'o', markersize = 0.3, color = 'black', label = 'file name')


plt.xlabel('wavelength/nm')
plt.ylabel('counts')
plt.legend()
plt.show()

