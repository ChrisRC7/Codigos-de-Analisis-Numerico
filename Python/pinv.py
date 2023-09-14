import numpy as np

def Pseudoinversa(A, b):
    # Paso 1: Aproximar la pseudoinversa de A
    X = (1 / np.linalg.norm(A, 'fro') ** 2) * A.T
    iterMax = 1000
    tol = 1e-15
    Im = np.eye(A.shape[0])

    for k in range(1, iterMax):
        X = X.dot(2 * Im - A.dot(X))
        er = np.linalg.norm(A.dot(X).dot(A) - A, 'fro')

        if er < tol:
            break

    pInv = X

    # Paso 2: Solución del problema
    x = X.dot(b)

    # Paso 3: Diferencia
    err = np.linalg.norm(A.dot(x) - b)

    return pInv, x, err

# Ejemplo de sistema de ecuación
A = np.array([[1, 1],
              [3, 3]])

b = np.array([2, 0]) 

#print(Pseudoinversa(A, b))

A2=np.array([[4,-2, 1], 
            [20, -7, 12],
            [-8, 13, 17,]])
b2= np.array([3, 25, 22]).T



print(Pseudoinversa(A2, b2))
