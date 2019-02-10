
clc;
clear;

%»æÖÆRastriginº¯ÊýÍ¼ÐÎ
x=[-5:0.1:5];
y=x;
[X,Y]=meshgrid(x,y);
[row,col]=size(X);
for l =1:col
    for h=1:row
        z(h,l)=Rastrigin([X(h,l),Y(h,l)]);
    end
end
mesh(X,Y,z);
%view([-15.5 30]);
shading interp
