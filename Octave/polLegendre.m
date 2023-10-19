function pk=polLegendre(n)
  pkg load symbolic
  syms x
  p0=1; p1=x;
  for k=2:n
    pk=simplify(((2*k-1)*x*p1-(k-1)*p0)/k);
    p0=p1;
    p1=pk;
  end
end

