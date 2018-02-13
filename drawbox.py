# -*- coding: utf-8 -*-


import os
import pandas as pd
from PIL import Image, ImageDraw


def draw_boxes(path):
    
    file_pic = '\\image_1000\\TB1..FLLXXXXXbCXpXXunYpLFXX.jpg' # 图片的地址
    file_text = '\\txt_1000\\TB1..FLLXXXXXbCXpXXunYpLFXX.txt' # 描述文件的地址
    if not os.path.exists(path + file_pic):
        print('无法找到图片')
        return
    if not os.path.exists(path + file_text):
        print('无法找到描述文件')
        return
    
    img = Image.open(path + file_pic)
    draw = ImageDraw.Draw(img)
    text_point = pd.read_csv(path + file_text, header=None)
    
    for idx, row in text_point.iterrows():
        
        point = row.loc[range(8)].tolist() # 依次读取八个点的数据
        x = [point[i] for i in [0, 2, 4, 6]]
        y = [point[i] for i in [1, 3, 5, 7]]
        point = [(a,b) for a,b in zip(x,y)] + [(x[0], y[0])]
        draw.line(point, fill=256, width=5)
        
    return img

if __name__ == '__main__':
    
    path = 'D:\\datastore\\1802tianchi\\ICPR_text_train_part1_20180211' # 文件夹地址

    img = draw_boxes(path)
    img.save(path + '\\demo.jpg')
    img.show()
    
    