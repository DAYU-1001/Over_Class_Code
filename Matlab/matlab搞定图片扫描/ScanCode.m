clc;
clear all;
filename='TestPic.jpg';%ͼƬ���ƣ�Ĭ���������ͬһ�ļ�����
img=imread(filename);%����ͼƬ
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
disp('ת������');
res(:,:,1)=R(:,:);
res(:,:,2)=G(:,:);
res(:,:,3)=B(:,:);
imwrite(res,'stripes2.png');%����ͼƬ
disp('ͼƬ�ѱ���');


