import numpy as np
import sust_adelante as sust

def sust_atras(A, b):
    m= len(b)
    x= np.zeros(m)
    for i in range(m - 1, -1, -1 ):
        aux= 0
        for j in range(i + 1, m):
            aux += A[i, j] * x[j]
        x[i] = (1 / A[i, i]) * (b[i] - aux)
    return x

def triang_sup(A , b):
    m= np.size(A, 1)
    At= np.hstack((A, b.reshape(-1, 1)))

    for i in range(m - 1):
        for j in range(i + 1, m):
            p= At[j , i] / At[i , i]
            for k in range(i, m + 1):
                At[j, k] -= p * At[i , k]
    Ar= At[:, :m]
    br= At[:, m]

    return Ar, br

def triang_inf(A, b):
    m = np.size(A, 1)
    At = np.hstack((A, b.reshape(-1, 1)))

    for i in range(1, m):
        for j in range(0, i):
            p = At[j, i] / At[i, i]
            for k in range(i, m + 1):
                At[j, k] -= p * At[i, k]
    
    Ar = At[:, :m]
    br = At[:, m]

    return Ar, br

def elim_gauss_sust_atras(A, b):
    At, bt= triang_sup(A, b)
    #print(At)
    x= sust_atras(At, bt)
    return x

def elim_gauss_sust_adelante(A, b):
    At, bt= triang_inf(A, b)
    print(At)
    print(bt)
    x= sust.sust_hacia_adelante(At, bt)
    return x

A=np.array([[2,-6, 12, 16], 
            [1, -2, 6, 6],
            [-1, 3, -3, -7], 
            [0, 4, 3, -6]])
b= np.array([70, 26, -30, -26]).T
#Ar, br= triang_sup(A, b)
#x= sust_atras(Ar, br)
y= elim_gauss_sust_atras(A, b)
y2= elim_gauss_sust_adelante(A, b)
print(y)
print(y2)

A2=np.array([[4,-2, 1], 
            [20, -7, 12],
            [-8, 13, 17,]])
b2= np.array([3, 25, 22]).T
Ar2, br2= triang_sup(A2, b2)
x2= sust_atras(Ar2, br2)

#print(x2)