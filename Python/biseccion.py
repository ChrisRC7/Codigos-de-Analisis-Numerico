def biseccion(a, b, func, tol, iterMax):
    """
    Aproximacion del cero de la funcion func utilizando el metodo de la Biseccion
    Estructura: [xk,error,k]=biseccion(a,b,func,tol,iterMax)
    Parametros: a,b = intervalo [a,b] donde se busca el cero
            func = funcion a la que se le aproxima el cero
            tol = tolerancia de aproximacion
            iterMax = iteraciones maximas a realizar
            xk = aproximacion del cero
            error = error del metodo dado por |func(xk)|
            k = iteraciones realizadas
    """
    f= lambda x: eval(func)

  
    if f(a)*f(b) <0:
        for i in range(1, iterMax):
            xk= (a+b)/2
            if f(a)*f(xk) < 0:
                b= xk
            else:
                a= xk
            error= abs(f(xk))
            if error < tol:
                return (xk, error, tol)
        return (xk, error, iterMax)
