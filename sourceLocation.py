import json
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

cdict = {'red':   [(0.0,  .1, .1),
                   (0.5,  .5, .5),
                   (1.0,  .5, .5)],

         'green': [(0.0,  0.0, 0.0),
                   (1.0,  0.0, 0.0)],

         'blue':  [(0.0,  0.0, 0.0),
                   (1.0,  0.0, 0.0)],
                   
         'alpha':  [(0.0,  0.0, 0.0),
                   (1.0,  0.5, 0.5)],
                   }

def plume(s_x, s_y, t_x, t_y, windspeed, windDir):
    x = t_x - s_x
    y = t_y - s_y
    alpha = math.radians(windDir)
    a_x = x * math.cos(alpha) - y * math.sin(alpha)
    a_y = x * math.sin(alpha) - y * math.cos(alpha)
    return plumeModel(a_x, a_y, windspeed)

def plumeModel(x, y, windspeed):
    eComp = math.exp(-((1/2)+(y/2)))
    return (1/(math.pi*windspeed)) * eComp

def mapPlume(s_x, s_y, windspeed, windDir, n, m):
    colorgrad = mpl.colors.LinearSegmentedColormap("Concentration", cdict)
    plumeMap = np.zeros((m, n))
    for i,v in enumerate([x / 10.0 for x in range(5, n*10, 10)]):
        for j,k in enumerate([x / 10.0 for x in range(5, m*10, 10)]):
            plumeMap[j, i] = plume(s_x, s_y, v, k, windspeed, windDir)
            print(str(v))
            print(str(i) + ", " + str(j) + " = " + str(plumeMap[j,i]))
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    data = plumeMap
    plt.imshow(data, cmap=colorgrad)
    plt.show()


if __name__ == "__main__":
    print(plumeModel(25.7, 32.1, 10))
    print(plumeModel(25.7, 1, 10))
    #mapPlume(25.7, 32.1, 10, 330, 200, 100)
