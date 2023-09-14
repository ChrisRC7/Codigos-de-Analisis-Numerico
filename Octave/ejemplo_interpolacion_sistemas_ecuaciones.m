%Pares ordenados (xi,yi), i=0,1,...,n
clc; clear;
%x=[1 3 4 8]; y=[2 5 7 -2];
x=[0.2 0.3 0.4 0.5 0.6 0.7 0.8]; y=log(asin(x))./log(x);
n=length(x)-1;
A=[];
for k=n:-1:0
  A=[A (x').^k];
end

a=linsolve(A,y');
xv=0.2:0.01:0.8;
fv=log(asin(xv))./log(xv);
yv=polyval(a,xv); %p(x)=a3*x^3+a2*x^2+a1*x+a0, donde a=[a3 a2 a1 a0]
hold on
plot(xv,yv,'r')
plot(xv,fv,'b')

