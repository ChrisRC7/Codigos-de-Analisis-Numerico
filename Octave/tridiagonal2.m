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

