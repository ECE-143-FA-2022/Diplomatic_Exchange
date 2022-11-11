#  !!! First of all !!! 
#  run this in terminal:
#        pip install mpl-chord-diagram

from collections import defaultdict
import pandas as pd
import os
import sys
sys.path = [os.path.abspath("..")] + sys.path

import matplotlib.pyplot as plt
import numpy as np

from mpl_chord_diagram import chord_diagram


data = pd.read_csv('COW-country-codes.csv', sep=",")
data = data.values.tolist()

countries=defaultdict(int)
coun_name=[]
for idx in range(len(data)):
    countries[data[idx][0]]=data[idx][1]
    if data[idx][0] not in coun_name:
        coun_name.append(data[idx][0])

data1 = pd.read_csv('Diplomatic_Exchange_2006v1.csv', sep=",")
data1 = data1.values.tolist()

exchange_alltime=defaultdict(int)
for idx in range(len(data1)):
    exchange_alltime[(data1[idx][0],data1[idx][1])]+=data1[idx][4]

exchange=np.zeros((len(countries),len(countries)))
for i in range(len(countries)):
    
    for j in range(len(countries)):
        
        exchange[i][j]=exchange_alltime[(countries[coun_name[i]],countries[coun_name[j]])]
N1=10
N2=50


chord_diagram(exchange[:N1,:N1], coun_name[0:N1],fontsize=7)
plt.savefig("10.png", dpi=600,
        transparent=True,
        bbox_inches='tight', pad_inches=0.02)
chord_diagram(exchange[:N2,:N2], coun_name[0:N2],fontsize=3)
plt.savefig("50.png", dpi=600,
        transparent=True,
        bbox_inches='tight', pad_inches=0.02)
plt.show()
