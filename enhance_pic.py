import cv2
from math import *
import numpy as np
import os
from skimage import data, exposure, img_as_float
import json, io
from collections import defaultdict
import matplotlib as plt

def cal_x(x ,y, degree, w, h):
    x1 = x / fabs(cos(radians(degree)))
    x2 = (h - y - x * fabs(tan(radians(degree)))) * fabs(sin(radians(degree)))
    return str(round(x1 + x2))

def cal_y(x, y, degree, w, h):
    y1 = (x - y * fabs(tan(radians(degree)))) * fabs(sin(radians(degree)))
    y2 = y / fabs(cos(radians(degree)))
    return str(round(y1 + y2))

def cal_x2(x, y, degree, w, h):
    x1 = (y - x * fabs(tan(radians(degree)))) * fabs(sin(radians(degree)))
    x2 = x / fabs(cos(radians(degree)))
    return str(round(x1 + x2))

def cal_y2(x ,y, degree, w, h):
    y1 = y / fabs(cos(radians(degree)))
    y2 = (w - x - y * fabs(tan(radians(degree)))) * fabs(sin(radians(degree)))
    return str(round(y1 + y2))

def count_rotate(count, new_count, h ,w, degree):
    filename = 'D:/dataset2/json/' + '%06d' % count + '.json'
    #print('count = ', count )
    with io.open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()
    for d1 in data:
        d = defaultdict(list)
        x1 = int(d1[7:].split(',')[0])
        y1 = int(d1[7:].split(',')[1])
        x2 = int(d1[7:].split(',')[2])
        y2 = int(d1[7:].split(',')[5])
        # print(x1)
        # print(y1)
        # print(x2)
        # print(y2)
        if degree>0:
            d[''].append(
                cal_x2(x1, y1, degree, w, h) + ',' + cal_y2(x1, y1, degree, w, h) + ',' + cal_x2(x2, y1, degree, w, h) + ','
                + cal_y2(x2, y1, degree, w, h) + ',' + cal_x2(x2, y2, degree, w, h) + ',' + cal_y2(x2, y2, degree, w, h)
                + ',' + cal_x2(x1, y2, degree, w, h) + ',' + cal_y2(x1, y2, degree, w, h))

        else:
            d[''].append(
                cal_x(x1, y1, degree, w, h) + ',' + cal_y(x1, y1, degree, w, h) + ',' + cal_x(x2, y1, degree, w, h) + ','
                + cal_y(x2, y1, degree, w, h) + ',' + cal_x(x2, y2, degree, w, h) + ',' + cal_y(x2, y2, degree, w, h)
                + ',' + cal_x(x1, y2, degree, w, h) + ',' + cal_y(x1, y2, degree, w, h))
        json_str = json.dumps(d)
        with open('D:/dataset2/json/' + '%06d' % new_count + '.json', 'a') as f:
            f.write(json_str + '\n')

def rotate_img(img_path, degree):
    #img_path = 'D:/dataset/000001.jpg'
    img = cv2.imread(img_path)
    h = img.shape[0]
    w = img.shape[1]
    #print(img)
    height, width = img.shape[:2]
    heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))
    widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))
    matRotation = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)
    # print(matRotation)
    matRotation[0, 2] += (widthNew - width) / 2
    matRotation[1, 2] += (heightNew - height) / 2
    imgRotation = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderMode=cv2.BORDER_REPLICATE)
    #imgRotation = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(0, 0, 0))
    #image = cv2.resize(imgRotation, (112, 112))
    # if (degree <= 0) & (degree >= -20):
    #     a = 112/(1+2*tan(radians(abs(degree))))
    #     b = (112-a)/2
    #     image = image[int(b):int(a+b), int(b):int(a+b)]
    # elif (degree > 0) & (degree <= 20):
    #     b = 112/(tan(radians(degree))+1/(tan(radians(degree)))+2)
    #     a = 112 - 2*b
    #     image = image[int(b):int(a+b), int(b):int(a+b)]
    return imgRotation, h, w

def brightness(img_path):
    img = cv2.imread(img_path)
    img1 = exposure.adjust_gamma(img, 1.25)  # 调暗
    img2 = exposure.adjust_gamma(img, 1.5)  # 调亮
    img3 = exposure.adjust_gamma(img, 0.75)  # 调暗
    img4 = exposure.adjust_gamma(img, 0.5)  # 调亮
    return img1, img2, img3, img4

def wap(img_path):
    img = cv2.imread(img_path)
    height, width= img.shape[:2]
    pts1 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    pts2 = np.float32([[0 + width*0.1, height*0.1], [width-width*0.1, height*0.1], [0, height], [width, height]])
    pts3 = np.float32([[0, 0], [width, 0], [width*0.1, height-height*0.1], [width-width*0.1, height-height*0.1]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    M2 = cv2.getPerspectiveTransform(pts1, pts3)
    res1 = cv2.warpPerspective(img, M, (width, int(height)), borderMode=cv2.BORDER_REPLICATE)
    res2 = cv2.warpPerspective(img, M2, (width, int(height)), borderMode=cv2.BORDER_REPLICATE)
    return res1, res2

def count_json_brightness(count, new_count):
    filename = 'D:/dataset2/json/' + '%06d' % count + '.json'
    with io.open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()
    for d1 in data:
        d = defaultdict(list)
        d[''].append(d1[7:].split(',')[0] + ',' + d1[7:].split(',')[1] + ',' + d1[7:].split(',')[2] + ','
                     + d1[7:].split(',')[3] + ',' + d1[7:].split(',')[4] + ',' + d1[7:].split(',')[5]
                     + ',' + d1[7:].split(',')[6] + ',' + d1[7:].split(',')[7][:-4])
        json_str = json.dumps(d)
        with open('D:/dataset2/json/' + '%06d' % new_count + '.json', 'a') as f:
            f.write(json_str + '\n')

def main():
    train_data_dir = "D:/dataset/"
    count = 3751
    for root, dirs, files in os.walk(train_data_dir):
        for file in files:
            img = root + file
            print(root + file)
            #print(file[:6])
            #旋转 计算坐标
            for degree in range(-10, 11):
                if degree == 0:
                    continue
                output_path = 'D:/dataset2/' + '%06d' % count + '.jpg'
                img_afterdegree, h, w = rotate_img(img, degree)
                count_rotate(int(file[:6]), count, h, w, degree)
                count += 1
                #print(output_path)
                cv2.imwrite(output_path, img_afterdegree)
            #wap 计算坐标
            # img_after_wap1, img_after_wap2 = wap(img)
            # output_path = 'D:/dataset2/' + '%06d' % count + '.jpg'
            # count+=1
            # cv2.imwrite(output_path, img_after_wap1)
            # output_path = 'D:/dataset2/' + '%06d' % count + '.jpg'
            # count+=1
            # cv2.imwrite(output_path, img_after_wap2)
            #亮度 坐标不变
            # img_after_brightness, img_after_brightness2, img_after_brightness3, img_after_brightness4 = brightness(img)
            # output_path = 'D:/dataset2/' + '%06d' % count + '.jpg'
            # count_json_brightness(int(file[:6]), count)
            # count += 1
            # cv2.imwrite(output_path, img_after_brightness)
            # output_path = 'D:/dataset2/' + '%06d' % count + '.jpg'
            # count_json_brightness(int(file[:6]), count)
            # count += 1
            # cv2.imwrite(output_path, img_after_brightness2)
            # output_path = 'D:/dataset2/' + '%06d' % count + '.jpg'
            # count_json_brightness(int(file[:6]), count)
            # count += 1
            # cv2.imwrite(output_path, img_after_brightness3)
            # output_path = 'D:/dataset2/' + '%06d' % count + '.jpg'
            # count_json_brightness(int(file[:6]), count)
            # count += 1
            # cv2.imwrite(output_path, img_after_brightness4)


if __name__ == '__main__':
    main()
