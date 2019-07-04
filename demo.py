import os
import matplotlib.pyplot as plt
from PIL import Image
path = 'D:/dataset2/json/json'
path2 = 'D:/大四下/中国软件杯/Bank_Card_OCR/数据标注程序/dataset2'
for root, dirs, files in os.walk(path):
    for file in files:
        #print(file[:-4])
        srcFile = path+'/'+file
        #print(file[3:])
        print(srcFile)
        # pic = Image.open(srcFile)
        # new_pic = pic.draft("RGB", (200, 200))
        # new_pic.save(path2+'/'+file)
        # print(path2+'/'+file)
        #plt.imshow(new_pic)
        #plt.show()
        #print(pic)
        dstFile = path+'/'+ '%06d' % (int(file[:-5])-2) +'.json'
        print(dstFile)
        os.rename(srcFile, dstFile)
