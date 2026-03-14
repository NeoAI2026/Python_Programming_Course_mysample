# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 00:36:42 2026

@author: a0936
"""

x1, y1 = eval(input("第一個點座標:"))
x2, y2 = eval(input("第二個點座標:"))
distance = ((x2 - x1)**2+(y2 - y1)**2)**0.5
print(distance)