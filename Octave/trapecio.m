function I=trapecio(f,a,b)
  % f='log(asin(x))/log(x)'; a=0.2; b=0.8;
  fnum=str2func(['@(x)' f]);
  I=(b-a)*(fnum(b)+fnum(a))/2;
end

