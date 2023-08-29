import sympy as sp
from sympy.utilities import lambdify

def newton(x0,func,tol,iterMax):
    """
    Aproximacion del cero de la funcion func utilizando el metodo de la Newton
    Estructura: [xk,error,k]=newton(x0,func,tol,iterMax)
    Parametros: x0 = valor inicial
            func = funcion a la que se le aproxima el cero
            tol = tolerancia de aproximacion
            iterMax = iteraciones maximas a realizar
            xk = aproximacion del cero
            error = error del metodo dado por |func(xk)|
            k = iteraciones realizadas

    Ejemplo: [xk,error,k]=newton(0.5,'exp(x)-x-10',1e-10,1000)
    """
    # Convertir el texto a expresiones simbólicas
    fsym = sp.sympify(func)
    fdsym = fsym.diff()
    
    # Crear funciones numéricas a partir de expresiones simbólicas
    f = lambdify( fsym, "numpy")
    fd = lambdify( fdsym, "numpy")

    xk=x0
    for i in range(1,iterMax):
        #Verificar que fd(xk) no sea cero
        xk=xk-f(xk)/fd(xk)
        error=abs(f(xk))
        if error<tol:
           return (xk, tol, i)
    return (xk, tol, iterMax)
