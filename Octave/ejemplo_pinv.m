%Ejemplo de sistema de ecuacion
clc; clear;

A=[1 1; 3 3];
b=[2 0]';

%Paso 1: Aproximar la pseudoinversa de A

X=(1/norm(A,'fro')^2)*A';
iterMax=1000;
tol=1e-15;
Im=eye(size(A,1));
for k=1:iterMax
  X=X*(2*Im-A*X);
  er=norm(A*X*A-A,'fro')
  if er<tol
    break
  end
end
display('Pseudoinversa')
pInv=X

%Paso 2: Solucion del problema
x=X*b

%Paso3: Diferencia
err=norm(A*x-b)

