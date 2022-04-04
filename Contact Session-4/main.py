import pandas as pd
import numpy as np
import os
import sys
import chardet
from matplotlib.pyplot import plot as plt

FOLDER_NAME = "\Contact Session-4"
os.chdir(os.getcwd() + FOLDER_NAME)
   
""" PERFORMING LINEAR REGRESSION FROM SCRATCH """

def remove_outliers(x):
    return 100.0 if x > 100.0 else x

def define_X_Y(header: str):
    X = []
    for i in file.head(20)[header]:
        X.append(remove_outliers(float(i)))
    return X

def calculate_slope(y:int,ybar:float,x:float,xbar:float):
    # calcualte using 
    # m = E(y - ybar)(x - xbar) / (x - xbar) ^ 2
    # where £ = summation, xbar = x mean , ybar = y mean
    index: int = 0
    num: int = 0
    den: int = 0
    
    while(index < len(y)):
        num += (y[index] - ybar) * (x[index] - xbar)
        den += np.power((x[index] - xbar), 2)
        index += 1
        pass
        
    return num / den

def calculate_intercept(y: int,x: int, m:int):
    c = y - (m * x)
    return c

def generate_equation_of_line(m:int, c:int, x:int):
    return (m * x) + c

def new_equation_of_line(m:int, c:int, value_x:list[int]):
    y = []
    for x in value_x:
        y.append(generate_equation_of_line(m,c,x))
    return y

def goodness_of_fit(ypred, ybar, y):
    # calculates the spread between the ypreicted and the yobserver
    num = 0
    den = 0
    index = 0
    while index < len(ypred):
        num += np.power(ypred[index] - ybar, 2)
        den += np.power(y[index] - ybar, 2)
        index += 1
    return num / den

file = pd.read_csv(r"incd.csv",encoding='Windows-1252')

X = define_X_Y('Age-Adjusted Incidence Rate(Ê) - cases per 100,000')
y = define_X_Y('Average Annual Count')
    
Xbar = np.mean(X)
ybar = np.mean(y)

print(np.mean(X))
print(np.mean(y))

m = calculate_slope(y,ybar,X,Xbar)
c = calculate_intercept(ybar,Xbar,calculate_slope(y,ybar,X,Xbar))
x_input = X

print(m,c)

# reduce the error

print(new_equation_of_line(m,c,x_input)) # takes in  m,c, and x then ouputs the new y (predicted value)

ypred = new_equation_of_line(m,c,x_input)

print(goodness_of_fit(ypred,ybar,y))

# visuals

