import numpy as np

def sust_hacia_adelante(A, b):
    m = len(b)
    x = np.zeros((m, 1))
    for i in range(m):
        aux= 0
        for j in range(m-1, -1, -1):
            aux+= A[i, j]*x[j]
        x[i]= (1/A[i,i])*(b[i]-aux)
        #x[i] = (b[i] - np.dot(A[i, :i], x[:i])) / A[i, i]
    return x

A = np.array([[2, 0, 0],
              [1, 5, 0],
              [4, -5, 6]])

b = np.array([4, 7, 27])

x = sust_hacia_adelante(A, b)
#print(x)