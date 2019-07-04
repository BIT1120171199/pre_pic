import json
from PIL import Image
import os, io
from tqdm import tqdm

def json_files_from_folder(folder):
	for root, dirs, files in os.walk(folder):
		for f in files:
			yield f

def image_from_file(fname):
	if not os.path.exists(fname):
		print(fname+'not exists.')
		return None
	image = Image.open(fname)
	return image

def load_json_file(filename):
	with io.open(filename, 'r', encoding='utf-8') as f:
		data = f.readlines()
		return data

def points_rank(points):
	tmp = sorted(zip(points[::2], points[1::2]), key=lambda x: x[0])
	# left points
	l = sorted(tmp[:2], key=lambda x: x[1])
	# right points
	r = sorted(tmp[2:], key=lambda x: x[1])
	return [l[0][0], l[0][1], r[0][0], r[0][1], r[1][0], r[1][1], l[1][0], l[1][1]]

def samples(folder):
    for json_file in json_files_from_folder(gt_dir):
        image_file = img_dir + json_file[:-5] + '.jpg'
        json_file = gt_dir + json_file
        image = image_from_file(image_file)
        #print(image)
        label = load_json_file(json_file)
        #print(image_file)
        #print(label)
        if not image or not label:
            continue
        positions = []
        for d1 in label:
            points = []
            points.append(int(d1[7:].split(',')[0]))
            points.append(int(d1[7:].split(',')[1]))
            points.append(int(d1[7:].split(',')[2]))
            points.append(int(d1[7:].split(',')[3]))
            points.append(int(d1[7:].split(',')[4]))
            points.append(int(d1[7:].split(',')[5]))
            points.append(int(d1[7:].split(',')[6]))
            points.append(int(d1[7:].split(',')[7][:-4]))
            if points[0] < 0:
                print(points)
                continue
            # print(points_rank(points))
            positions.append(points_rank(points))
        #print(positions)
        yield image, positions

def summary(folder):
    count = 0
    max_len = 0
    max_height = max_width = mean_height = mean_width = 0
    for image, positions in tqdm(samples(folder)):
        count += 1
        width, height = image.size
        #print(width)
        #print(height)
        mean_height += height
        mean_width += width
        if width > max_width:
            max_width = width
        if height > max_height:
            max_height = height
        # if len(chars) > max_len:
        #     max_len = len(chars)
    mean_height /= count
    mean_width /= count
    print('max height: %d, max width: %d, mean_height: %f, mean_width: %f'%( max_height, max_width, mean_height, mean_width))
    print('total samples: %d'%count)

if __name__ == '__main__':
    gt_dir = 'D:/dataset2/json/'
    img_dir = 'D:/dataset/'
    summary(gt_dir)

