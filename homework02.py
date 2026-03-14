# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 00:50:57 2026

@author: a0936
"""
pump = eval(input("請輸入心臟跳動次數："))
yeartime = pump*(24*60*60)*365.25*80
print("80歲心跳次數:",yeartime)


tempC = eval(input("請輸入攝氏溫度:"))
print("華氏溫度為:",tempC*1.8+32)


areahouse = eval(input("請輸入房屋坪數:"))
areahouseM = areahouse*3.3058
print(f"你的房子為{areahouseM}平方公尺")


W = eval(input("請輸入體重:"))
H = eval(input("請輸入身高:"))
print("您的BMI = ",W/H**2*100)


a, b, c = 2, 5, 2
print("數學公式一計算結果:",(-b+((b**2.0) - 4*a*c)**0.5)/2*a)


a, b = 100, 50
print("數學公式二計算結果:",(a**2-b**2)/(a+b))