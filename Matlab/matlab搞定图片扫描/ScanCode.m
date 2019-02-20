clc;
clear all;
filename='TestPic.jpg';%ͼƬ���ƣ�Ĭ�ϵ�ǰ�ļ���
img=imread(filename);%ͼƬ����
R=img(:,:,1);
G=img(:,:,2);
B=img(:,:,3);

[x,y,z]=size(img);

for i=1:x
    for j=1:y
        if ((R(i,j)>=140)&&(R(i,j)<=255)&&(G(i,j)<100)&&(B(i,j)<100))%����Ǻ�ɫ��ͼ�£�
            R(i,j)=255;
            G(i,j)=70;
            B(i,j)=70;
        else
            %Gray = R*0.299 + G*0.587 + B*0.114    �Ҷ���RGBת����ʽ
            gray=R(i,j)*0.299+G(i,j)*0.587+B(i,j)*0.114;
            if gray>120  %120Ϊһ�Ҷ���ֵ����������һ��ֵ��ȫ����Ϊ��ɫ��120Ϊһ����ֵ
                R(i,j)=255;
                G(i,j)=255;
                B(i,j)=255;
            end
        end
    end
end
disp('ת������');
for i=1:x
    disp(['��ɫ����',num2str(i/x*100),'%']);%��ʾ���ǽ���
    for j=1:y
        res(i,j,1) = R(i,j);
        res(i,j,2) = G(i,j);
        res(i,j,3) = B(i,j);
    end
end
imwrite(res,'stripes2.png');%����ͼƬ
disp('ͼƬ�ѱ���');