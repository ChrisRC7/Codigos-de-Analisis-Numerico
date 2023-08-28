function [xk,error,k]=newton(x0,func,tol,iterMax)
  %
  % Aproximacion del cero de la funcion func utilizando el metodo de la Newton
  %
  % Estructura: [xk,error,k]=newton(x0,func,tol,iterMax)
  %
  % Parametros: x0 = valor inicial
  %             func = funcion a la que se le aproxima el cero
  %             tol = tolerancia de aproximacion
  %             iterMax = iteraciones maximas a realizar
  %             xk = aproximacion del cero
  %             error = error del metodo dado por |func(xk)|
  %             k = iteraciones realizadas
  %1
  % Ejemplo: [xk,error,k]=newton(0.5,'exp(x)-x-10',1e-10,1000)

  pkg load symbolic

  % Texto a Simbolico
  fsym=sym(func);
  fdsym=diff(fsym);

  % Simbolico a Numerico
  f=matlabFunction(fsym);
  fd=matlabFunction(fdsym);

  xk=x0;

  for k=1:iterMax
    % Verificar que fd(xk) no sea cero
    xk=xk-f(xk)/fd(xk);
    error=abs(f(xk));
    if error<tol
      break
    end
  end

end

