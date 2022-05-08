import os
import shutil
import codecs

from tqdm import tqdm
from YOLO2COCO.yolov5_2_coco import YOLOV5ToCOCO


def copy_2_dir_file(img_folder: str, xml_folder: str, num_of_dataset: int,
                    output_img: str = "output_dir/images", output_xml: str = "output_dir/labels"):
    # 检查文件是否存在
    if not os.path.exists(output_img):
        os.makedirs(output_img)
    if not os.path.exists(output_xml):
        os.makedirs(output_xml)

    # 创建文件名列表
    img_list = []
    xml_list = []

    for a in os.listdir(img_folder):
        img_list.append(os.path.split(a.replace("\\", "/"))[1])
    for a in os.listdir(xml_folder):
        xml_list.append(os.path.split(a.replace("\\", "/"))[1])

    for a in tqdm(range(num_of_dataset)):
        basename = os.path.splitext(img_list[a])[0]
        shutil.copy(os.path.join(img_folder, img_list[a]), output_img)
        shutil.copy(os.path.join(xml_folder, "{}.xml".format(basename)), output_xml)


def create_train_val_class_txt(img_folder: str, category_list: list, output_folder=None):
    """
    img_folder
     ├─train
     └─val
    """
    # 检查output_folder是否存在/待创建
    if output_folder is None:
        output_folder = os.path.abspath(os.path.join(img_folder, os.pardir))
    elif not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 创建文件列表并写入
    with codecs.open(os.path.join(output_folder, "train.txt"), mode="w", encoding="utf-8") as train_f:
        train_path = os.path.join(img_folder, "train")
        for filepath in tqdm(os.listdir(train_path), desc="train", postfix=train_path):
            train_f.write(os.path.join(train_path, filepath))
            train_f.write("\n")
    with codecs.open(os.path.join(output_folder, "val.txt"), mode="w", encoding="utf-8") as val_f:
        val_path = os.path.join(img_folder, "val")
        for filepath in tqdm(os.listdir(val_path), desc="val", postfix=val_path):
            val_f.write(os.path.join(val_path, filepath))
            val_f.write("\n")
    with codecs.open(os.path.join(output_folder, "classes.txt"), mode="w", encoding="utf-8") as class_f:
        for category in tqdm(category_list, desc="classes", postfix=category_list):
            class_f.write(category)
            class_f.write("\n")


if __name__ == '__main__':
    # 从源文件夹创建测试文件夹
    # copy_2_dir_file(img_folder="final_dataset/images", xml_folder="final_dataset/labels", num_of_dataset=200)

    # 创建train.txt和val.txt
    # create_train_val_class_txt(img_folder="dataset_211115_example/images",
    #                            category_list=["cat", "dog", "horse", "person"],
    #                            output_folder="dataset_211115_example/")

    # 转换YOLOv5数据集到COCO数据集
    # yolo2coco = YOLOV5ToCOCO("dataset_211115_example")
    # yolo2coco.generate()

    pass
