clc;
clear;

%»æÖÆAckleyº¯ÊýÍ¼ÐÎ
x=[-8:0.1:8];
y=x;
[X,Y]=meshgrid(x,y);
[row,col]=size(X);
for l =1:col
    for h=1:row
        z(h,l)=Ackley([X(h,l),Y(h,l)]);
    end
end
mesh(X,Y,z);
%view([-15.5 30]);
shading interp
