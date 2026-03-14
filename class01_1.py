# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a = 1
print(a)

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.square(x)
plt.plot(x, y)
plt.show()

print("圓柱體體積為:",3.14*10*10*5)
print("圓柱體表面積為:",3.14*10*10*2 + 2*3.14*10*5)