# 这是基于YOLOX，经修改过后可以用于关键点检测的模型，对应标注软件：Labelme
## 准备数据集
1. 将特征点标注软件labelme标注后的json文件放入datasets/jsons文件夹,将图片文件放入datasets/pictures文件夹
2. 如果图片数量和json文件数量不一样，运行**datasets/find.py**,找出两者不一样的文件名
3. 运行**datasets/json_txt.py**,这一步是为了将json文件转换为每行只包含标签和特征点坐标的txt文件
4. 运行**datasets/test.py**，在程序内修改特征点数，此程序确保转换后的txt文件中每行的元素个数一定是**标签+特征点个数*2**
5. 将验证过的txt文件和图片放入**data**文件夹下，并在里面创建**class_names.txt**文件，在其中写入类名，一行一个，不用双引号
6. 运行**datasets/coco.py**,在程序里**修改特征点数**和训练集所占比例即可按照data中的文件生成coco文件夹
   
## 修改配置文件
1. 使用**exps/example/custom/yolox_s.py**文件作为模型配置文件修改里面的**self.num_classes**参数为自己的类别数量， **self.num_apexes**为特征点数，**self.max_epoch**为轮次数
2. 修改**yolox/data/datasets/coco_classes.py**文件，在**COCO_CLASSES**类中加上自己的类名，注意此处的顺序需要和class_names.txt中的顺序相同

## 训练
1. `python tools/train.py -f exps/example/custom/yolox_s.py -d 0 -b 4 --fp16  `

## 推理
1. `python tools/demo.py image -f exps/example/custom/yolox_s.py -c YOLOX_outputs/yolox_s/last_epoch_ckpt.pth --path datasets/coco/images --conf 0.6 --nms 0.1 --tsize 640 --save_result --device gpu `

## 转成ONNX格式,看结构图
1. `python3 tools/export_onnx.py --output-name yolox.onnx -f exps/example/custom/yolox_s.py -c YOLOX_outputs/yolox_s/last_epoch_ckpt.pth`

## 转成TensoRT格式，加速推理
1. `python3 tools/trt.py -f exps/example/custom/yolox_s.py -c best_ckpt.pth `
