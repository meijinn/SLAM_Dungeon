from PIL import Image
import numpy as np
import csv


pgm_name="map"
img = Image.open('./'+pgm_name+'.pgm')
np_img = np.array(img)

print(np_img)
print(np_img.shape)

#csvファイルとして保存
np.savetxt('out.csv',np_img,delimiter=',')


list=[]
for row in np_img:
    list.append(row)

with open('./'+pgm_name+'.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(list)

"""
#白csv作成
for row in range(0,np_img.shape[0]):
    #1のとき長さ測定
    w_flag=0
    for column in range(0,np_img.shape[1]):
        if w_flag==0:
            #白を初めて検出
            if np_img[row,column]>=250:
                w_flag=1
                w_length=1
                init_row=row
                init_column=column

        if w_flag==1:
            w_length=w_length+1
            #白でないなら
            if np_img[row,column]<=250:
                w_flag=0
                w_length=w_length-1
                w_temp=[init_row,init_column,w_length]
                white_list.append(w_temp)

            
        
with open('./'+pgm_name+'_white_list.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(white_list)






#黒csv作成
black_list=[]
for row in range(0,np_img.shape[0]):
    #1のとき長さ測定
    b_flag=0
    for column in range(0,np_img.shape[1]):
        if b_flag==0:
             #白を初めて検出
            if np_img[row,column]<=10:
                b_flag=1
                b_length=1
                init_row=row
                init_column=column

        if b_flag==1:
            b_length=b_length+1
            #白でないなら
            if np_img[row,column]>=10:
                b_flag=0
                b_length=b_length-1
                b_temp=[init_row,init_column,b_length]
                black_list.append(b_temp)

            
        
with open('./'+pgm_name+'_black_list.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(black_list)
"""
