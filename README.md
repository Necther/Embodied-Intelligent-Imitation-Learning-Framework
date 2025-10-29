# 迅摹（EmbodLearn）

## 1、项目介绍

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EmbodLearn为机器人模仿学习提供了一个全面且易用的解决方案。它不仅降低了技术门槛，还通过模块化设计和先进算法实现，为研究者和工程师提供了强大的工具。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;随着模仿学习技术的不断发展，我们可以期待这个框架在更多复杂任务和机器人平台上的应用，进一步推动智能机器人技术的普及和发展。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果你对机器人学习感兴趣，不妨尝试这个框架，开启你的智能机器人开发之旅！

## 2、环境配置

配置虚拟环境：

```
# 创建虚拟环境
conda create -y -n lero python=3.10.16
# 激活虚拟环境
conda activate lero
# 安装相关软件包
pip install lerobot==0.1.0
sudo apt update
sudo apt install -y ffmpeg \
  libavformat-dev \
  libavcodec-dev \
  libavdevice-dev \
  libavutil-dev \
  libswscale-dev \
  libswresample-dev \
  libavfilter-dev
pip install av==14.0.0
pip install -e .
pip install -e ".[aloha, pusht]"
pip install -e ".[dynamixel]"
# conda install -c conda-forge ffmpeg=7.1
# pip uninstall opencv-python
pip install opencv-python==4.10.0.82
pip install numpy ==1.24.0
```

## 3、操作流程

### 3.1 查询机械臂端口号

将机械臂按照第一章操作连接上电脑，然后运行脚本find_motors_bus_port.py，该脚本用于查找通信端口号：

```
python lerobot/scripts/find_motors_bus_port.py
```

运行后会出现下面截图：

![image](https://github.com/Necther/Embodied-Intelligent-Imitation-Learning-Framework/blob/main/tmp/img/image-20251029103115919.png)

接着按照提示，我们先拔掉随从臂的线，然后按下Enter键，出现：

![image](https://github.com/Necther/Embodied-Intelligent-Imitation-Learning-Framework/blob/main/tmp/img/image-20251029103132778.png)

可以看出，我们的随从臂的端口号为/dev/ttyACM0；然后接上刚拔下来的线。重复上述操作，检测主控线的通信端口号：

![image](https://github.com/Necther/Embodied-Intelligent-Imitation-Learning-Framework/blob/main/tmp/img/image-20251029103149638.png)

可以看出主控臂的端口号为/dev/ttyACM2。

接着，我们对端口号赋予权限，运行下列命令：

```
sudo chmod 666 /dev/ttyACM0
sudo chmod 666 /dev/ttyACM2
```

### 3.2 查询相机的端口号

运行opencv.py脚本：

```
python lerobot/common/robot_devices/cameras/opencv.py
```

运行结果如下：

![image](https://github.com/Necther/Embodied-Intelligent-Imitation-Learning-Framework/blob/main/tmp/img/image-20251029103244839.png)

可以看到检测到了3个摄像头，其中一个是电脑自带的摄像头。拍摄的照片文件保存在outputs/images_from_opencv_cameras文件夹下：

![image](https://github.com/Necther/Embodied-Intelligent-Imitation-Learning-Framework/blob/main/tmp/img/image-20251029103301322.png)

相机0视角图

![image](https://github.com/Necther/Embodied-Intelligent-Imitation-Learning-Framework/blob/main/tmp/img/image-20251029103317224.png)

相机4视角图

### 3.3 修改相关配置文件，并测试通信是否正常

通过3.1和3.2的操作，知道主控臂的端口号为/dev/ttyACM2，随从臂的端口号为/dev/ttyACM0，顶部的视角相机索引值为0，前视角相机的索引值为4。（可根据自己的设备自由配置，支持扩展）

接着对下列脚本中的参数进行修改：

./lerobot/scripts文件夹下：

修改calibration.py:

将第7行和第8行的电机端口号进行相应的修改，leader_port和follower_port分别表示主控臂和随从臂的端口号。

修改configure_arm.py:

修改第7行和第8行的电机端口号；

修改connect.py:

修改第5行和第6行的电机端口号；

./lerobot/configs/robot文件夹下：

修改koch.yaml:

修改第13行和第26行电机端口号，并修改第39行和第45行的相机索引号，其中laptop表示俯视图，phone表示前视图。

修改完毕了，我们可以运行configure_arm.py脚本，来检查机械臂通信是否正常：

```
python lerobot/scripts/configure_arm.py
```

运行结果如下：

![image](https://github.com/Necther/Embodied-Intelligent-Imitation-Learning-Framework/blob/main/tmp/img/image-20251029103538831.png)

### 3.4标定机械臂

标定机械臂是为了让机械臂在采取数据时能够行动一致，尽可能较小误差。我们需要运行下列命令进行标定工作:

```
python lerobot/scripts/calibration.py
```

运行后会出现下列提示：

![image](https://github.com/Necther/Embodied-Intelligent-Imitation-Learning-Framework/blob/main/tmp/img/image-20251029103630945.png)

需要分别将随从臂和主控臂移动到零位、旋转位和重置位，各位置的分布如下图所示：

![image](https://github.com/Necther/Embodied-Intelligent-Imitation-Learning-Framework/blob/main/tmp/img/image-20251029103644832.png)



最后可以得到标定文件：

![image](https://github.com/Necther/Embodied-Intelligent-Imitation-Learning-Framework/blob/main/tmp/img/image-20251029103704489.png)

可以看到最后输出的两行列表，代表主从机械臂各关节角度，两者之间的角度之差不大于10度即可。若需要重新进行标零位，需要手动删除.cache/calibration/koch文件夹，清除零位标定文件，再次重复标定即可。

## 3.5遥操与数据集采集

### 3.5.1遥操

现在机械臂的配置已经完成，接下来我们进行遥操测试，主要测试移动主控臂时随从臂是否会移动，移动角度偏差大不大。

运行命令：

```
python lerobot/scripts/control_robot.py teleoperate \
  --robot-path lerobot/configs/robot/koch.yaml
```

示例如下：

![image](https://github.com/Necther/Embodied-Intelligent-Imitation-Learning-Framework/blob/main/tmp/img/image-20251029103759290.png)

遥操示例截图：

![image](https://github.com/Necther/Embodied-Intelligent-Imitation-Learning-Framework/blob/main/tmp/img/image-20251029103810422.png)

### 3.5.2数据集采集

在确定遥操动作没问题后，开始进行数据集采取：

运行下列命令：

```
python lerobot/scripts/control_robot.py record \
  --robot-path lerobot/configs/robot/koch.yaml \
  --fps 30 \
  --repo-id local_user/koch_test_t \
  --tags tutorial \
  --warmup-time-s 5 \
  --episode-time-s 18 \
  --reset-time-s 5 \
  --num-episodes 100 \
  --push-to-hub 0
```

参数解释：

```
--robot-path: 机械臂配置文件，包含电机配置和相机设置
--fps：相机帧率
--repo-id：数据集存放文件夹
--tags：标签
--warmup-time-s：机械臂热身启动时间，可根据自己采集任务自行修改。
--episode-time-s：采集某个任务数据所需时间，可自行修改。
--reset-time-s：重置某个任务环境时间，可自行修改。
--num-episodes：采集数据集集数，自行修改，最好在80-100集。
--push-to-hub：数据集是否推送到huggingface，0表示不推送，1表示推送
```

运行效果示例图：

```
python lerobot/scripts/control_robot.py record \
  --robot-path lerobot/configs/robot/koch.yaml \
  --fps 30 \
  --repo-id local_user/koch_mutli \
  --tags tutorial \
  --warmup-time-s 5 \
  --episode-time-s 40 \
  --reset-time-s 8 \
  --num-episodes 50 \
  --push-to-hub 0
```

## 4、训练

运行下列命令启动训练脚本：

```
python lerobot/scripts/train.py \
  dataset_repo_id=local_user/koch_test1 \
  policy=act_koch_real \
  env=koch_real \
  hydra.run.dir=outputs/train/act_koch_test \
  hydra.job.name=act_koch_test \
  device=cuda \
  wandb.enable=true
```

```
--dataset_repo_id：存储训练数据路径；
--policy：训练策略；
--env：指定训练环境；
--hydra.run.dir：指定了实验结果和日志的保存目录；
--hydra.job.name：指定作业名称，用于区分不同训练任务；
```

对于单目标任务，我们采集了100组数据作为训练集，对于多目标任务进行多个数据集混合训练。训练日志如下：

![image](https://github.com/Necther/Embodied-Intelligent-Imitation-Learning-Framework/blob/main/tmp/img/image-20251029104012507.png)

## 5、推理

使用下列命令进行推理：

```
python lerobot/scripts/control_robot.py record \
  --robot-path lerobot/configs/robot/koch.yaml \
  --fps 30 \
  --repo-id local_user/koch_test3 \
  --tags tutorial eval \
  --warmup-time-s 5 \
  --episode-time-s 15 \
  --reset-time-s 5 \
  --num-episodes 10 \
  --push-to-hub 0 \
  -p outputs/train/act_koch_test/checkpoints/last/pretrained_model
```

上述命令与之前用于记录训练数据集的命令几乎相同。主要变化有两点：

新增了 -p 参数用于指定策略检查点路径（例如 -p outputs/train/eval_koch_test/checkpoints/last/pretrained_model）。如果已将模型检查点上传到 Hub，也可直接使用模型仓库路径（例如 -p ${HF_USER}/act_koch_test）。

数据集名称以 eval 开头以表明这是推理过程（例如 --repo-id ${HF_USER}/eval_koch_test）。

以执行向杯子中倒茶这个任务为例，下图展示了ACT算法训练的模型的效果：

![image](https://github.com/Necther/Embodied-Intelligent-Imitation-Learning-Framework/blob/main/tmp/img/image-20251029104059788.png)

​                                                               ACT算法在真实环境任务的效果图