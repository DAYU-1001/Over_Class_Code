function y= Rosenbrock(x)
[row,col]=size(x);
if row>1
    error('输入的参数错误');
end

y=100*(x(1,2)-x(1,1)^2)^2+(x(1,1)-1)^2;
y=-y;




