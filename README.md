# pre_pic
<br>深度学习竞赛图像预处理，包括旋转、透视变换以及亮度调整等，在原有基础上增强320倍。项目所用任务为目标检测，因此json文件为ground_truth四点坐标，具体的:</br>
<br>demo.py:批量重命名文件</br>
<br>decode_json.py:对label进行解析，统计样本信息</br>
<br>txt_to_json.py:将标记好的txt格式label转为json格式</br>
<br>enhance.py:图像增强核心代码，同时对ground_truth进行计算</br>
<br>img_line.py:对增强前后的图像和ground_truth进行验证，结果如下:</br>
<h3>旋转前</h3>

![Image text](https://github.com/HuiyanWen/pre_pic/blob/master/000001.jpg)

<h3>旋转后</h3>

![Image text](https://github.com/HuiyanWen/pre_pic/blob/master/000001_after.jpg)


