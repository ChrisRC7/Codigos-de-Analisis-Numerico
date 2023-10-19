function I=trapecio_compuesto_iterativo(f,a,b)
  % f='log(asin(x))/log(x)'; a=0.2; b=0.8;
  tol=1e-17; iterMax=1e10; iterMin=1;
  for k=iterMin:iterMax
    Inew=trapecio_compuesto(f,a,b,k);
    if k>iterMin
      er=abs(Inew-I)
      if er<tol
        I=Inew;
        break;
      end
    end
    I=Inew;
  end
end

