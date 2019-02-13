function ObjVal = Sphere(Chrom)

% Dimension of objective function

   
      % function 11, sum of 100* (x(i+1) -xi^2)^2+(1-xi)^2 for i = 1:Dim (Dim=10)
      % n = Dim, -10 <= xi <= 10
      % global minimum at (xi)=(1) ; fmin=0
      ObjVal=sum((Chrom.^2)')';
     
end