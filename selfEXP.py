from YOLOX.exps.default.yolox_s import Exp as MyEXP


class Exp(MyEXP):
    def __init__(self):
        super(Exp, self).__init__()
        self.num_classes = 4  # 类别数量
        self.max_epoch = 200  # 训练总轮数
        self.data_dir = "dataset_211115_example_COCO_format"  # 数据集文件夹
        self.train_ann = "instances_train2017.json"  # 训练集标签文件名
        self.val_ann = "instances_val2017.json"  # 验证集标签文件名
        self.eval_interval = 5  # 每隔5轮验证一次
