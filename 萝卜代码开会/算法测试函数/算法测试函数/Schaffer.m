function ObjVal = Schaffer(Chrom)

    Dim=size(Chrom,2);
   
% Compute population parameters
   [Nind,Nvar] = size(Chrom);


      % function 11, sum of 100* (x(i+1) -xi^2)^2+(1-xi)^2 for i = 1:Dim (Dim=10)
      % n = Dim, -10 <= xi <= 10
      % global minimum at (xi)=(1) ; fmin=0
      Mat1 = Chrom(:,1:Nvar-1);
      Mat2 = Chrom(:,2:Nvar);
     f=Mat1.^2+Mat2.^2;
%       if Dim == 2
% %          ObjVal = 100*(Mat2-Mat1.^2).^2+(1-Mat1).^2;
% %          ObjVal = Mat1.^2+2*(Mat2.^2)-0.3*cos(3*pi*Mat1)-0.4*cos(4*pi*Mat2)+0.7;
%          ObjVal = ((sin(sqrt(f))).^2-0.5)/((1+0.001*f).^2)+0.5*(Dim-1);
%       else
%          ObjVal = sum((100*(Mat2-Mat1.^2).^2+(1-Mat1).^2)')';
         ObjVal =sum(((sin(sqrt(f))).^2-0.5)/((1+0.001*f).^2),2)+0.5*(Dim-1);
%       end  
end