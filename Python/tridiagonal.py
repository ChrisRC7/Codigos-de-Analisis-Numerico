import numpy as np

def matrizTridiagonal(x):
    A= np.zeros((x,x))
    x-=1
    A[0,0] = 10  
    A[0,1] = 2
    A[x, x-1]= -1
    A[x, x]= 10

    for i in range(1 , x):
        A[i, i-1] = -1
        A[i, i] = 10
        A[i , i+1] = 2

    return A





def metodoQR(A):
    m= len(A)
    U= np.zeros_like(A)
    Q= np.zeros_like(A)

    U[:, 0]= A[:, 0]

    Q[:, 0] = U[:, 0] / np.linalg.norm(U[:, 0])

    for i in range(1 , m):
        sum= np.zeros_like(A[:, 0])
        for j in range(i):
            colum1= A[:, i]
            colum2= Q[:, j]
            sum+= (np.dot(colum1, colum2) * Q[:, j])

        U[:, i] = A[:, i] - sum
        Q[:, i] = U[:, i] / np.linalg.norm(U[:, 0])

    R=  np.dot(Q.T, A)

    return (Q, R)

def SolveVe():
    A= matrizTridiagonal(100)
    b= np.ones(100)
    Q, R= metodoQR(A)
    c= np.dot(Q.T, b)
    print(np.linalg.solve(R, c))

    #A= matrizTridiagonal(10)
    #b= np.ones(10)
    A2= np.linalg.inv(A)
    print(np.dot(A2,b))
    x = np.linalg.solve(A, b)

    # 2. Calcula la norma de la diferencia entre Ax y b
    diferencia = np.linalg.norm(np.dot(A, x) - b)

    # 3. Comprueba si la norma es aproximadamente cero
    tolerancia = 1e-6  # Define una tolerancia pequeña para considerar cero
    if diferencia < tolerancia:
        print("La solución es correcta.")
    else:
        print("La solución no es correcta.")

def sol_Jacobi(A, b):
    tol= 1e-10
    iterMax= 1000
    d= np.diag(A)
    D= np.diag(d)
    Lmu= A-D
    Dinv= np.diag(1/d)
    M= -Dinv*Lmu
    c= Dinv*b
    m= len(b)
    xk= np.zeros((m,1))
    for i in range(iterMax):
        xk= M*xk+c
        er= np.linalg.norm(np.dot(A,xk) -b)
        if er<tol:
            return xk
        
    return xk

SolveVe()