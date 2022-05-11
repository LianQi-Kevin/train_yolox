### build YOLOX on Jetson Nano

##### step - 1. Install PyTorch1.8.0 & torchvision0.9.0
[PyTorch for Jetson - version 1.11 now available](https://forums.developer.nvidia.com/t/pytorch-for-jetson-version-1-11-now-available/72048/2)

##### step - 2. clone and install YOLOX
1. clone
    ```shell
    git clone -b 0.3.0 https://github.com/Megvii-BaseDetection/YOLOX.git
    cd YOLOX
    ```

2. 在`{YOLOX}/requirements.txt`中 \
   注释 `numpy`, `torch`, `torchvision`, `opencv_python`, `tensorboard`
3. Install
    ```shell
    # {pip3_path} is common `which python3`
    sudo {pip3_path} install pythran
    sudo {pip3_path} install -v -e .
    ```

##### step - 3. install torch2trt

```shell
git clone https://github.com/NVIDIA-AI-IOT/torch2trt
cd torch2trt
sudo python3 setup.py install
```



