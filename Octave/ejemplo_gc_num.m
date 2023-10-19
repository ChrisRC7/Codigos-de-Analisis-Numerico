%Ejemplo del gradiente conjugado
clc; clear;
pkg load symbolic
warning('off','all')

f=@(x,y) (x-2)^4+(x-2*y)^2;
syms x y
fs=sym(f); %Representación simbolica
grSym=gradient(fs,[x y]);
gr=matlabFunction(grSym);
xk=3; yk=0; %Valores iniciales
iterMax=1000; tol=10^-10;

%Paso 1: Definir gk y dk iniciales
gk=gr(xk,yk);
dk=-gk;

xt_k=[xk yk]';

for k=1:iterMax
  %Paso 2: Calcular alpha_k (ak)
  ak=calc_ak(f,xt_k,dk,gk);

  %Paso 3: calcular nuevo x^k+1 (xt_kp1)
  xt_kp1=xt_k+ak*dk;

  %Paso 4: Verificar condicion de salida ||gradient en x^k+1||<tol
  norm_grad=norm(gr(xt_kp1(1),xt_kp1(2)))
  if norm_grad<tol
    break
  end

  %Paso 5: Actualizar gk y dk
  gk_new=gr(xt_kp1(1),xt_kp1(2));
  bk=norm(gk_new)^2/norm(gk)^2;
  dk_new=-gk_new+bk*dk;

  %Paso 6: Actualizar datos para la siguiente iteracion
  gk=gk_new;
  dk=dk_new;
  xt_k=xt_kp1;
end





