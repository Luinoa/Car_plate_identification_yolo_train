import os
import os.path
import re
import shutil

import cv2
from tqdm import tqdm


def listPathAllfiles(dirname):
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            result.append(apath)
    return result

if __name__ == '__main__':
    data_path = r'E:\BaiduNetdiskDownload\CCPD2019\no_plate'
    save_path = r'D:\Projects\yolov5\datasets\ccpd'

    images_save_path = os.path.join(save_path, "images")
    labels_save_path = os.path.join(save_path, "labels")

    if not os.path.exists(images_save_path): os.makedirs(images_save_path)
    if not os.path.exists(labels_save_path): os.makedirs(labels_save_path)

    images_files = listPathAllfiles(data_path)

    cnt = 1
    for name in tqdm(images_files):
        if name.endswith(".jpg") or name.endswith(".png"):
            img = cv2.imread(name)
            height, width = img.shape[0], img.shape[1]

            x = round(0, 6)
            y = round(0, 6)
            w = round(0, 6)
            h = round(0, 6)

            txtfile = os.path.join(labels_save_path, "no_plate_" + str(cnt).zfill(6) + ".txt")
            imgfile = os.path.join(images_save_path,
                                   "no_plate_" + str(cnt).zfill(6) + "." + os.path.basename(name).split(".")[-1])

            open(txtfile, "w").write("")
            shutil.copy(name, imgfile)  # 移动文件到别的位置，且重命名

            cnt += 1

