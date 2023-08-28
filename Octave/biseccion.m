function [xk,error,k]=biseccion(a,b,func,tol,iterMax)
  %
  % Aproximacion del cero de la funcion func utilizando el metodo de la Biseccion
  %
  % Estructura: [xk,error,k]=biseccion(a,b,func,tol,iterMax)
  %
  % Parametros: a,b = intervalo [a,b] donde se busca el cero
  %             func = funcion a la que se le aproxima el cero
  %             tol = tolerancia de aproximacion
  %             iterMax = iteraciones maximas a realizar
  %             xk = aproximacion del cero
  %             error = error del metodo dado por |func(xk)|
  %             k = iteraciones realizadas
  %
  % [xk,error,k]=biseccion(2,3,'exp(x)-x-10',1e-10,1000)


  % Texto a Numerico
  f=str2func(['@(x)' func]);

  if f(a)*f(b)<0
    for k=1:iterMax
      xk=(a+b)/2;
      if f(a)*f(xk)<0
        b=xk;
      else
        a=xk;
      end
      error=abs(f(xk));
      if error<tol
        break
      end
    end
  else
    xk='N/A';
    error='N/A';
    k='N/A'
    display('No se cumple la condicion de Bolzano con los datos dados')
  end

end

