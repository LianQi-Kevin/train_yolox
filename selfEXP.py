# from YOLOX.exps.default.yolox_s import Exp as MyEXP
from yolox.exp import Exp as MyEXP
import os.path


class Exp(MyEXP):
    def __init__(self):
        super(Exp, self).__init__()
        self.num_classes = 4  # 类别数量
        self.max_epoch = 300  # 训练总轮数
        self.data_dir = "dataset_211115_example_COCO_format"  # 数据集文件夹
        self.train_ann = "instances_train2017.json"  # 训练集标签文件名
        self.val_ann = "instances_val2017.json"  # 验证集标签文件名
        self.eval_interval = 5  # 每隔5轮验证一次
        self.no_aug_epochs = 30  # 最后30轮不使用图像增强
        self.depth = 0.33   # yolox_s
        self.width = 0.50   # yolox_s
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]  # yolox_s
