% Escribir el código para generar una matriz
% tridiagonal, donde la digonal principal tenga el valor
% de 5, y las diagonales adyacentes igual a 1

clc; clear;

n=15; %Tamaño de la matriz
A=zeros(n);

%Primera fila
A(1,1)=5; A(1,2)=1;
%Ultima Fila
A(n,n)=5; A(n,n-1)=1;

for i=2:n-1
  A(i,i)=5; A(i,i-1)=1; A(i,i+1)=1;
end

A

