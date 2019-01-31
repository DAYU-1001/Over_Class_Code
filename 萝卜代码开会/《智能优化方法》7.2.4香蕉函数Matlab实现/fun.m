function y = fun( x )
%y=x(1).^2+x(2).^2;
y=0;
for i=1:4
    y=y+(100*(x(i+1)-x(i))^2+(x(i)-1)^2);
end

