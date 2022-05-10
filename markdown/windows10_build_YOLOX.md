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

#### Step - 3. clone and install YoloX 0.3.0

```shell
git clone -b 0.3.0 https://github.com/Megvii-BaseDetection/YOLOX.git
cd YOLOX
set PYTHONIOENCODING=UTF-8
pip install -v -e .
```

> windows平台安装的错误修复 \
> https://github.com/Megvii-BaseDetection/YOLOX/issues/879