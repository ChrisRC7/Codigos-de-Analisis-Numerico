import sympy as sp
import numpy as np


def variables_simbolicas(variables):
    """ Definir variables, a partir de un texto """
    n=len(variables)
    tam=np.arange(0,n,2)
    v_var=[]
    for i in tam:
        v_var.append(sp.Symbol(variables[i]))    
    return v_var


def gradiente(f,v_var):
    """ Definir gradiente de una funcion"""
    n=len(v_var)
    g=[]
    for i in np.arange(0,n,1):
        g.append(sp.diff(f,v_var[i]))
    return g

"""Ejemplo básico"""
t='x y'
v_var = variables_simbolicas(t)
print(t)
print(v_var)

funcion='(x-2)^4+(x-2*y)^2'


x0=0
y0=0

f=sp.sympify(funcion)

print(f.subs([(v_var[0],x0), (v_var[1],y0)]))
f_n=sp.lambdify(v_var, f)
print(f_n)
print(f_n(x0,y0))



g=gradiente(f,v_var)
print(g)
g_n=sp.lambdify(v_var, g)
print(g_n(x0,y0))
