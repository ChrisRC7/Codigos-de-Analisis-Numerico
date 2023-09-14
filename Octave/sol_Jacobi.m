function xk=sol_Jacobi(A,b)
  tol=1e-10; iterMax=1000;
  d=diag(A);
  D=diag(d);
  LmU=A-D;
  Dinv=diag(1./d);
  M=-Dinv*LmU;
  c=Dinv*b;
  m=length(b);
  xk=zeros(m,1);
  for k=1:iterMax
    xk=M*xk+c;
    er=norm(A*xk-b);
    if er<tol
      break
    end
  end
end

