import os
import cv2

def delete_corrupted_images(img_dir):
    img_names = [f for f in os.listdir(img_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    corrupted_files = []

    for img_name in img_names:
        img_path = os.path.join(img_dir, img_name)
        image = cv2.imread(img_path)
        if image is None:
            corrupted_files.append(img_path)
            print(f"Deleting corrupted image: {img_path}")
            os.remove(img_path)

    print(f"Total corrupted images deleted: {len(corrupted_files)}")

if __name__ == "__main__":
    img_dir = 'E:/BaiduNetdiskDownload/CCPD2019/ccpd_np'
    delete_corrupted_images(img_dir)