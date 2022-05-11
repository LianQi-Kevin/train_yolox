
# OOM ERROR 

---
~~##### step - 1. install torch2trt~~
```shell
git clone https://github.com/NVIDIA-AI-IOT/torch2trt
cd torch2trt
sudo python3 setup.py install
```

~~##### step - 2. Convert model~~
```shell
python3 {YOLOX}/tools/trt.py -f <your_exp_file> -c <your_ckp>
```
> `python3 ../tools/trt.py -f ./selfEXP.py -c ./best_ckpt.pth`

