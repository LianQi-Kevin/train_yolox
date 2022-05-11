### Installation

#### Step - 1. create conda env

```shell
conda create -n YoloX python=3.8 
```

#### Step - 2. install PyTorch and torchvision

```shell
# cuda 10.2
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=10.2 -c pytorch
```

#### step - 3. install TensorRT and torch2trt
TensorRT: [Win 10 配置TensorRT环境](https://blog.csdn.net/qianshuqinghan/article/details/104776612?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-0&spm=1001.2101.3001.4242)

torch2trt:
```shell
git clone https://github.com/NVIDIA-AI-IOT/torch2trt
cd torch2trt
python3 setup.py install --plugins
```


#### Step - 3. clone and install YoloX 0.3.0

```shell
git clone -b 0.3.0 https://github.com/Megvii-BaseDetection/YOLOX.git
cd YOLOX
set PYTHONIOENCODING=UTF-8
pip install -v -e .
```

> windows平台安装的错误修复 \
> https://github.com/Megvii-BaseDetection/YOLOX/issues/879