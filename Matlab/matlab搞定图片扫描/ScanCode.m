clc;
clear all;
filename='TestPic.jpg';%图片名称，默认与代码在同一文件夹下
img=imread(filename);%读入图片
R=img(:,:,1);
G=img(:,:,2);
B=img(:,:,3);
red=(R>=100).*(R<=255).*(G<110).*(B<110);
R(red==1)=255;
G(red==1)=70;
B(red==1)=70;
gray=R.*0.299+G.*0.587+B.*0.114;
white=(gray>120)-red;
R(white==1)=255;
G(white==1)=255;
B(white==1)=255;
disp('转换结束');
res(:,:,1)=R(:,:);
res(:,:,2)=G(:,:);
res(:,:,3)=B(:,:);
imwrite(res,'stripes2.png');%保存图片
disp('图片已保存');


