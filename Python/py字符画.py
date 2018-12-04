from PIL import Image
#468*472
#whale.jpg
chars = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`.'
#img=Image.open("whale.jpg")
img=Image.open("lqxy.jpg")

width,height = img.size
fb=open('img.txt','w')
temp=''
for j in range(0,height,4):#ÐÐ
    for i in range(0,width,4):#ÁÐ
        r,g,b=img.getpixel((i,j))
        gray=int(0.2126*r+0.7152*g+0.0722*b)
        char=chars[int((gray)/(256/len(chars)))]
        temp+=(char+' ')
    temp+='\n'
fb.write(temp)
#print(temp)