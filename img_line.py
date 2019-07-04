import os, io
import cv2
from math import *
img_path = 'D:/test/dataset2/000751.jpg'
img = cv2.imread(img_path)
print(img.shape[0])
print(img.shape[1])
h = 265
w = 353

def cal_x(x ,y, degree):
    x1 = x / fabs(cos(radians(degree)))
    x2 = (h - y - x * fabs(tan(radians(degree)))) * fabs(sin(radians(degree)))
    #print(round(x1 + x2))
    return round(x1 + x2)

def cal_y(x, y, degree):
    y1 = (x - y * fabs(tan(radians(degree)))) * fabs(sin(radians(degree)))
    y2 = y / fabs(cos(radians(degree)))
    #print(round(y1 + y2))
    return round(y1 + y2)

def cal_x2(x, y, degree):
    x1 = (y - x * fabs(tan(radians(degree)))) * fabs(sin(radians(degree)))
    x2 = x / fabs(cos(radians(degree)))
    #print(round(x1 + x2))
    return round(x1 + x2)

def cal_y2(x ,y, degree):
    y1 = y / fabs(cos(radians(degree)))
    y2 = (w - x - y * fabs(tan(radians(degree)))) * fabs(sin(radians(degree)))
    #print(round(y1 + y2))
    return round(y1 + y2)



def main():
    # ptStart = (40, 129)
    # ptEnd = (91, 129)
    point_x1 = 40
    point_x2 = 91
    point_y1 = 129
    point_y2 = 149
    degree = -10
    print(cal_x(point_x1, point_y1, degree))
    print(cal_y(point_x1, point_y1, degree))
    print(cal_x(point_x2, point_y1, degree))
    print(cal_y(point_x2, point_y1, degree))
    print(cal_x(point_x2, point_y2, degree))
    print(cal_y(point_x2, point_y2, degree))
    print(cal_x(point_x1, point_y2, degree))
    print(cal_y(point_x1, point_y2, degree))
    ptStart = (cal_x(point_x1, point_y1, degree), cal_y(point_x1, point_y1, degree))
    ptEnd = (cal_x(point_x2, point_y1, degree), cal_y(point_x2, point_y1, degree))
    point_color = (0, 255, 0)  # BGR
    thickness = 1
    lineType = 4
    cv2.line(img, ptStart, ptEnd, point_color, thickness, lineType)

    ptStart = (cal_x(point_x2, point_y1, degree), cal_y(point_x2, point_y1, degree))
    ptEnd = (cal_x(point_x2, point_y2, degree), cal_y(point_x2, point_y2, degree))
    point_color = (0, 255, 0)  # BGR
    thickness = 1
    lineType = 4
    cv2.line(img, ptStart, ptEnd, point_color, thickness, lineType)

    ptStart = (cal_x(point_x1, point_y1, degree), cal_y(point_x1, point_y1, degree))
    ptEnd = (cal_x(point_x1, point_y2, degree), cal_y(point_x1, point_y2, degree))
    point_color = (0, 255, 0)  # BGR
    thickness = 1
    lineType = 4
    cv2.line(img, ptStart, ptEnd, point_color, thickness, lineType)

    ptStart = (cal_x(point_x2, point_y2, degree), cal_y(point_x2, point_y2, degree))
    ptEnd = (cal_x(point_x1, point_y2, degree), cal_y(point_x1, point_y2, degree))
    point_color = (0, 255, 0)  # BGR
    thickness = 1
    lineType = 4
    cv2.line(img, ptStart, ptEnd, point_color, thickness, lineType)
    cv2.imshow('result.jpg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
