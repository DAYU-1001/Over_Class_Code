clc;
clear all;
filename='TestPic.jpg';%图片名称，默认当前文件夹
img=imread(filename);%图片读入
R=img(:,:,1);
G=img(:,:,2);
B=img(:,:,3);

[x,y,z]=size(img);

for i=1:x
    for j=1:y
        if ((R(i,j)>=140)&&(R(i,j)<=255)&&(G(i,j)<100)&&(B(i,j)<100))%如果是红色（图章）
            R(i,j)=255;
            G(i,j)=70;
            B(i,j)=70;
        else
            %Gray = R*0.299 + G*0.587 + B*0.114    灰度与RGB转换公式
            gray=R(i,j)*0.299+G(i,j)*0.587+B(i,j)*0.114;
            if gray>120  %120为一灰度阈值，若大于这一阈值，全部设为白色，120为一经验值
                R(i,j)=255;
                G(i,j)=255;
                B(i,j)=255;
            end
        end
    end
end
disp('转换结束');
for i=1:x
    disp(['颜色覆盖',num2str(i/x*100),'%']);%显示覆盖进度
    for j=1:y
        res(i,j,1) = R(i,j);
        res(i,j,2) = G(i,j);
        res(i,j,3) = B(i,j);
    end
end
imwrite(res,'stripes2.png');%保存图片
disp('图片已保存');