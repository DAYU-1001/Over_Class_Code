function y= Ackley(x)
[row,col]=size(x);
if row>1
    error('����Ĳ�������');
end

y=-20*exp(-0.2*sqrt((1/col)*(sum(x.^2))))-exp((1/col)*sum(cos(2*pi.*x)))+exp(1)+20;





