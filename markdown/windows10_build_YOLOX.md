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

> cuda10.2+cudnn8.2+tensorrt8.2.4

1. tensorrt
    1. 下载并解压缩：\
       [tensorrt-8.2.4.2.windows10.x86_64.cuda-10.2.cudnn8.2.zip](https://developer.nvidia.com/compute/machine-learning/tensorrt/secure/8.2.4/zip/tensorrt-8.2.4.2.windows10.x86_64.cuda-10.2.cudnn8.2.zip)
    2. 将解压缩后的文件放置到<安装文件夹>
    3. 将`<安装文件夹>/lib`添加到系统变量
    4. 切换到希望安装`tensorrt`的python环境
        ```shell
        pip install {tensorrt}/python/tensorrt-8.2.4.2-cp38-none-win_amd64.whl
        pip install {tensorrt}/uff/uff-0.6.9-py2.py3-none-any.whl
        pip install {tensorrt}/onnx_graphsurgeon/onnx_graphsurgeon-0.3.12-py2.py3-none-any.whl
        pip install {tensorrt}/graphsurgeon/graphsurgeon-0.4.5-py2.py3-none-any.whl
        ```

2. torch2trt

```shell
git clone https://github.com/NVIDIA-AI-IOT/torch2trt
cd torch2trt
python setup.py install --plugins
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