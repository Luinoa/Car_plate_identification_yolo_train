## Description
这是我们的数字图像处理课程项目的YOLOv5训练部分，包括了展示训练过程的`runs`文件夹、训练配置`ccpd.yaml`和处理数据集的脚本，它们均是以YOLOv5官方库为背景的，参见：  
> https://github.com/ultralytics/yolov5

## Dataset
我们使用使用的公开数据集有：
- CCPD2019
- CCPD2020
- SA-1B

其中，CCPD2019中的ccpd_base为蓝牌数据集，CCPD2020中的ccpd_green为我们提供了绿牌数据集，而背景集则由CCPD2019中的ccpd_np无牌车数据集和SA-1B数据集的无关图片组成。

### Process Dataset
在运行处理数据集脚本前需要安装re和shutil：  
`pip install re`  
`pip install shutil`  

请使用`get_dataset.py`处理CCPD中的目标数据集，注意将21行和23行的源和目标路径改成对应的路径，另外，在处理绿牌数据集时，请注意将51行开始的处理内容中的blue替换成green。  
请使用`get_dataset_no_plate`处理背景数据集，同样注意将19行和20行的源和目标路径改成对应的路径，你可以使用任意无关图片作为背景数据集，但是我们强烈推荐你在背景数据集中加入CCPD2019中的ccpn_np无牌数据集。
如果你要使用我们的配置进行训练，请将处理后的数据集放在YOLOv5根目录下的`datasets\ccpd`路径中。

由于CCPD数据集图片中有不能打开的图片，建议使用`delete_broken_files.py`去除。

## Train
在配置好YOLOv5后，执行命令：  
`python train.py --data ccpd.yaml --weights yolov5n.pt --img 640 --epochs 10 --batch-size 16`  
即可开始训练。  

你也可以在我们`runs/train/`中的训练过程中的模型的基础上进行训练，结果需要用`export`导出为onnx simplified模型。

## Runs
`runs`文件夹展示了我们的训练过程，其中： 

- `train-cls`是我们对YOLOv5模型训练的测试  
- `train`展示了我们的训练过程  
- `detect`为我们使用默认的detect方法得出的结果  

我们最终训练的yolov5m、yolov5s、yolov5n模型分别在`train`下的`exp8`、`exp13`、`exp16`文件夹中的`weights`文件夹中。

## License
​ 本项目基于Apache-2.0-license。
