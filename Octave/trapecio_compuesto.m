function I=trapecio_compuesto(f,a,b,m);
  % f='log(asin(x))/log(x)'; a=0.2; b=0.8;
  h=(b-a)/(m-1);
  xSoporte=a:h:b;
  I=0;
  for i=1:m-1
    I=I+trapecio(f,xSoporte(i),xSoporte(i+1));
  end
end

