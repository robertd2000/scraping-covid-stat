import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from main import main

c_list = main()

countries_list = []
counts_list = []

for item in c_list:
    countries_list.append(item['country'])
    counts_list.append(item['count'])
counts_list = [int(''.join(count.split(','))) for count in counts_list]
print(countries_list)
plt.pie(counts_list, labels=countries_list)
plt.axis('equal')
plt.show()
