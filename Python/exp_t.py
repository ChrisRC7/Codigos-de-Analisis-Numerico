
from mpmath import *

def exp_t(a, iterMax, tol):
    """
    La funcion exp_t aproxima el valor de e^a
    Sintaxis de la funcion: [sk,error,n]=exp_t(a,iterMax,tol)
    Parometros de entrada:
            a = nomero real
            iterMax = nomero entero positivo, que representa la cantidad de iteraciones moximas del motodo
            tol =  nomero real positivo, que es el criterio de parada del error, donde |S_(k+1)-S_(k)|<tol
    Parometros de salida:
            sk = aproximacion del valor e^a
            er = error dado por la formula |S_(k+1)-S_(k)|
            k = cantidad de iteraciones realizadas
    """
    sk = 0
    for i in range(iterMax):
        sk_n = sk + a**(i)/fac(i)
        err = abs(sk_n-sk)
        sk = sk_n
        if err < tol:
            return (float(sk), float(err), i)
    return (float(sk), float(err), iterMax)