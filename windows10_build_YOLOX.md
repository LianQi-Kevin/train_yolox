### Installation

#### Step - 1. create conda env

```shell
conda create -n YoloX python=3.8 
```

#### Step - 2. clone YoloX 0.3.0

```shell
git clone -b 0.3.0 https://github.com/Megvii-BaseDetection/YOLOX.git
```

#### Step - 3. install PyTorch and torchvision

```shell
# cuda 10.2
conda install pytorch==1.9.0 torchvision==0.10.0 torchaudio==0.9.0 cudatoolkit=10.2 -c pytorch
```

#### Step - 4. install YoloX

```shell
cd YOLOX
set PYTHONIOENCODING=UTF-8
pip install -v -e .
```

> windows平台安装的错误修复 \
> https://github.com/Megvii-BaseDetection/YOLOX/issues/879



---

##### 相关资料

* [如何评价旷视开源的YOLOX，效果超过YOLOv5?](https://www.zhihu.com/question/473350307)
* [YOLOX-TensorRT in Python](https://github.com/Megvii-BaseDetection/YOLOX/tree/main/demo/TensorRT/python)

