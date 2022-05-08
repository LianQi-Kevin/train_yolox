#### 1. 构建COCO数据集

参考: [COCO数据集标注格式详解----object instances](https://blog.csdn.net/qq_41375609/article/details/94737915)
> [转换YOLOv5数据集到COCO数据集](https://github.com/RapidAI/YOLO2COCO#yolov5%E6%A0%BC%E5%BC%8F%E6%95%B0%E6%8D%AEcoco)

#### 2. 构建EXP文件

1. 创建子类`Exp`, 继承`yolox.exp`的类`Exp`
2. 创建`__init__`方法，继承父类的参数
3. 重写`self.num_classes`,`self.max_epoch`

```python
# from yolox.exp import Exp as MyEXP
# 继承yolox_s的基础参数用以设置self.depth和self.width
from YOLOX.exps.default.yolox_s import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.num_classes = 4  # 类别数量
        self.max_epoch = 200  # 训练总轮数
        self.data_dir = "dataset_211115_example_COCO_format"  # 数据集文件夹
        self.train_ann = "instances_train2017.json"  # 训练集标签文件名
        self.val_ann = "instances_val2017.json"  # 验证集标签文件名
        self.eval_interval = 5  # 每隔5轮验证一次
```

#### 3. 下载权重文件

下载权重文件并放置`./weights/`

|Model |size |mAP<sup>val<br>0.5:0.95 |mAP<sup>test<br>0.5:0.95 | Speed V100<br>(ms) | Params<br>(M) |FLOPs<br>(G)| weights |
| ------        |:---: | :---:    | :---:       |:---:     |:---:  | :---: | :----: |
|[YOLOX-s](./exps/default/yolox_s.py)    |640  |40.5 |40.5      |9.8      |9.0 | 26.8 | [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_s.pth) |
|[YOLOX-m](./exps/default/yolox_m.py)    |640  |46.9 |47.2      |12.3     |25.3 |73.8| [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_m.pth) |
|[YOLOX-l](./exps/default/yolox_l.py)    |640  |49.7 |50.1      |14.5     |54.2| 155.6 | [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_l.pth) |
|[YOLOX-x](./exps/default/yolox_x.py)   |640   |51.1 |**
51.5**  | 17.3    |99.1 |281.9 | [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_x.pth) |
|[YOLOX-Darknet53](./exps/default/yolov3.py)   |640  | 47.7 | 48.0 | 11.1 |63.7 | 185.3 | [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_darknet.pth) |

|Model |size |mAP<sup>test<br>0.5:0.95 | Params<br>(M) |FLOPs<br>(G)| weights |
| ------        |:---: | :---:       |:---:     |:---:  | :---: |
|[YOLOX-Nano](./exps/default/nano.py) |416  |25.8  | 0.91 |1.08 | [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_nano.pth) |
|[YOLOX-Tiny](./exps/default/yolox_tiny.py) |416  |32.8 | 5.06 |6.45 | [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_tiny.pth) |

#### 4. 训练

```
python YOLOX/tools/train.py --exp_file selfEXP.py --batch-size 16 --fp16 --cache --occupy --ckpt weights/yolox_s.pth
```

#### 5. 使用`Tensorboard`查看训练日志

```
tensorboard --logdir ./YOLOX_outputs/yolox_s/tensorboard/
```

---

##### 参考资料

* [YOLOX骨干网backbone-PAFPN网络结构示意图（结合代码）](https://zhuanlan.zhihu.com/p/397020975)