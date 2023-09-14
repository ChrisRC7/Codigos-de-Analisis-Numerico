% Escribir el codigo para generar una matriz
% tridiagonal, donde A(i,i)=3*i,
% y las diagonales adyacentes igual a 1

clc; clear;

n=6; %Tamaño de la matriz
A=zeros(n);

%Primera fila
A(1,1)=3*1; A(1,2)=1;
%Ultima Fila
A(n,n)=3*n; A(n,n-1)=1;

for i=2:n-1
  A(i,i)=3*i; A(i,i-1)=1; A(i,i+1)=1;
end

A

% Asignar en un vector a,
% los valores de la diagonal principal
a=diag(A)

% Asignar en un vector b,
% los valores de la diagonal adyacente superior
a=diag(A,1)

% Asignar en un vector c,
% los valores de la diagonal adyacente inferior
a=diag(A,-1)









