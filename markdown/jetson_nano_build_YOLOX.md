### build YOLOX on Jetson Nano

##### step - 1. Install PyTorch1.8.0 & torchvision

```shell
# https://qengineering.eu/install-pytorch-on-jetson-nano.html
# install the dependencies (if not already onboard)
$ sudo apt-get install python3-pip libjpeg-dev libopenblas-dev libopenmpi-dev libomp-dev
$ sudo -H pip3 install future
$ sudo pip3 install -U --user wheel mock pillow
$ sudo -H pip3 install testresources
# above 58.3.0 you get version issues
$ sudo -H pip3 install setuptools==58.3.0
$ sudo -H pip3 install Cython
# install gdown to download from Google drive
$ sudo -H pip3 install gdown
# download the wheel
$ gdown https://drive.google.com/uc?id=1-XmTOEN0z1_-VVCI3DPwmcdC-eLT_-n3
# install PyTorch 1.8.0
$ sudo -H pip3 install torch-1.8.0a0+37c1f4a-cp36-cp36m-linux_aarch64.whl
# clean up
$ rm torch-1.8.0a0+37c1f4a-cp36-cp36m-linux_aarch64.whl
```

##### step - 2. clone and install YOLOX

```shell
git clone -b 0.3.0 https://github.com/Megvii-BaseDetection/YOLOX.git
cd YOLOX
pip3 install -v -e .
```

##### step - 3. install torch2trt

```shell
#git clone -b v0.3.0 https://github.com/NVIDIA-AI-IOT/torch2trt
git clone https://github.com/NVIDIA-AI-IOT/torch2trt
cd torch2trt
sudo python3 setup.py install --plugins
```

