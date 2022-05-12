#### step - 1. clone

```
git clone https://github.com/shouxieai/tensorRT_Pro.git
```

#### step - 2. 替换文件

使用[CMakeLists.txt](CMakeLists.txt)和 [Makefile](Makefile)替换`{tensorRT_Pro}/`下的对应文件

#### step - 3. 变更tensorrt8.x到tensorrt7.x

```shell
cd {tensorRT_Pro}
rm -rf src/tensorRT/onnx_parser
cp -r onnx_parser/onnx_parser_7.x src/tensorRT/onnx_parser
```

#### step - 4. 生成平台匹配的protoc文件

```shell
CD {tensorRT_Pro}/onnx
rm -rf pbout
mkdir -p pbout
protoc onnx-ml.proto --cpp_out=pbout
protoc onnx-operators-ml.proto --cpp_out=pbout
cp pbout/onnx-ml.pb.cc ../src/tensorRT/onnx/onnx-ml.pb.cpp
cp pbout/onnx-operators-ml.pb.cc ../src/tensorRT/onnx/onnx-operators-ml.pb.cpp
cp pbout/onnx-ml.pb.h ../src/tensorRT/onnx/onnx-ml.pb.h
cp pbout/onnx-operators-ml.pb.h ../src/tensorRT/onnx/onnx-operators-ml.pb.h
rm -rf pbout
```

#### step - 5. 编译

```shell
cd {tensorRT_Pro}
mkdir build && cd build
cmake ..
make yolo -j8
```

#### step - 6. python编译

1. 修改`{tensorRT_Pro}/src/application/tools/pybind11.hpp`

```objectivec
# line 159-161
//#include <Python.h>
//#include <frameobject.h>
//#include <pythread.h>
#include <python3.6/Python.h>
#include <python3.6/frameobject.h>
#include <python3.6/pythread.h>

# line 9216
//#include <datetime.h>
#include <python3.6/datetime.h>
```

> 或者用[pybind11.hpp](pybind11.hpp)替换`{tensorRT_Pro}/src/application/tools/pybind11.hpp`

2. 编译

```shell
cd {tensorRT_Pro}/build
make clean
make pyinstall -j8
```

编译最后会在`setup.py`报错， 但是库文件已经正确生成了
> 编译后的文件在: `{tensorRT_Pro}/python/trtpy/libtrtpyc.so`

```shell
cd {tensorRT_Pro}/python
sudo /usr/bin/python3 setup.py install  
```