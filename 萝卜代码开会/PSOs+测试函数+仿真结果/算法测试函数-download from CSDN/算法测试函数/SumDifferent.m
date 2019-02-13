function ObjVal = SumDifferent(Chrom,switc);

% Dimension of objective function

    [Row,Dim]=size(Chrom);
   
% Compute population parameters
%    [Nind,Nvar] = size(Chrom);
%       Mat1 = Chrom(:,1:Nvar-1);
%       Mat2 = Chrom(:,2:Nvar);
%      f=2*(Mat2.^2)+1;
%      m=2*(Mat1.^2)+1;
%       if Dim == 2
% %          ObjVal = 100*(Mat2-Mat1.^2).^2+(1-Mat1).^2;
% %          ObjVal = Mat1.^(2*(Mat2.^2)+1)+Mat2.^(2*(Mat1.^2)+1);
%          ObjVal = Mat1.^f+Mat2.^m;
%       else
%          ObjVal = sum(Mat1.^(2*(Mat2.^2)+1)+Mat2.^(2*(Mat1.^2)+1),2);
         temp=ones(Row,1)*(1:1:Dim);
         ObjVal = sum((abs(Chrom)).^(temp+1),2);
%       end   
%   temp=ones(4,1)*(1:1:5);

% End of function

