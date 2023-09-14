clc; clear
close all
tiempo1=[]; tiempo2=[]; tiempo3=[]; tiempo4=[]; tiempo5=[]; tiempo6=[];
tamano=100:100:500;
for m=tamano
   display(['Ejecuntando dimension m = ' num2str(m)])
   A=matriz_tridiag(m); b=[6 7*ones(1,m-2) 6]'; %Ax=b
   %Metodo de la Pseudoinversa
   tic; m1=sol_pseudoinversa(A,b,10^-10); t1=toc;
   tiempo1=[tiempo1 t1];
   %Metodo de Eliminacion Gaussiana
   tic; m2=sol_elim_gauss(A,b); t2=toc;
   tiempo2=[tiempo2 t2];
   %Metodo de Factorizacion LU
   tic; m3=sol_LU(A,b); t3=toc;
   tiempo3=[tiempo3 t3];
  %Metodo de Factorizacion QR
   tic; m4=sol_QR(A,b); t4=toc;
   tiempo4=[tiempo4 t4];
  %Metodo de Thomas
   tic; m5=sol_Thomas(A,b); t5=toc;
   tiempo5=[tiempo5 t5];
   %Comando de Octave
   tic; m6=mldivide(A,b); t6=toc;
   tiempo6=[tiempo6 t6];
end

%Grafica de Tiempo
hold on
plot(tamano,tiempo1,'r','LineWidth',2) %Pseudoinversa
plot(tamano,tiempo2,'b','LineWidth',2) %Elim Guass
plot(tamano,tiempo3,'y','LineWidth',2) %LU
plot(tamano,tiempo4,'k','LineWidth',2) %QR
plot(tamano,tiempo5,'g','LineWidth',2) %Thomas
plot(tamano,tiempo6,'m','LineWidth',2) %Octave
legend('Pseudoinversa','Elim. Gauss.', 'LU','QR','Thomas','Octave')
