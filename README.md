# 🤖 Embodied Intelligent Imitation Learning Framework

This project provides a complete pipeline from environment setup, device calibration, and data collection to training and inference with the different policy .

## 🌍 1. Environment Configuration

### 1.1 Create and Activate Environment

```python
conda create -y -n lero python=3.10.16
conda activate lero
```

### 1.2 Install Dependencies

```python
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

## ⚙️ 2. Operational Procedure

### 2.1 Query Robotic Arm Port Numbers

Run the following script to detect connected motor bus ports:

```python
python lerobot/scripts/find_motors_bus_port.py
```

The detected ports might appear as:

```python
Master Arm Port: /dev/ttyACM2
Slave Arm Port:  /dev/ttyACM0
```

Grant permissions:

```bash
sudo chmod 666 /dev/ttyACM0
sudo chmod 666 /dev/ttyACM2
```

### 2.2 Check Camera Port Numbers

Run the OpenCV detection script:

```bash
python lerobot/common/robot_devices/cameras/opencv.py
```

Captured frames are automatically saved to:

```
outputs/images_from_opencv_cameras/
```

For example:

- **Camera 0:** Top-view (laptop)
- **Camera 4:** Front-view (phone)



### 2.3 Configure Robot and Test Communication

Modify the configuration file:

```bash
lerobot/configs/robot/koch.yaml
```

- Update motor port numbers (`/dev/ttyACM0`, `/dev/ttyACM2`)
- Adjust camera indices (e.g., 0 for top view, 4 for front view)

Then test communication:

```bash
python lerobot/scripts/configure_arm.py
```

If successful, the arm status and torque readings will be displayed.

### 2.4 Calibrate the Robotic Arm

To ensure consistent operation and accurate data capture:

```bash
python lerobot/scripts/calibration.py
```



Follow on-screen prompts to move the arm to **zero**, **rotation**, and **reset** positions.



 The final calibration file will be stored in:

```
.cache/calibration/koch/
```



If recalibration is needed, delete this folder and repeat.

### 2.5 Remote Control & Data Collection

#### 2.5.1 Teleoperation Test

Verify that the slave arm follows the master arm’s movements:

```bash
python lerobot/scripts/control_robot.py teleoperate \
  --robot-path lerobot/configs/robot/koch.yaml
```





### 2.5.2 Record Dataset

After verifying teleoperation, record your demonstration dataset:

```bash
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

##### Parameter Explanation

| Parameter          | Description                                       |
| ------------------ | ------------------------------------------------- |
| `--robot-path`     | Configuration file for motors and cameras         |
| `--fps`            | Camera frame rate                                 |
| `--repo-id`        | Dataset storage directory                         |
| `--tags`           | Custom labels                                     |
| `--warmup-time-s`  | Robot warm-up time                                |
| `--episode-time-s` | Duration per recorded episode                     |
| `--reset-time-s`   | Environment reset duration                        |
| `--num-episodes`   | Number of recorded episodes                       |
| `--push-to-hub`    | Whether to upload to Hugging Face (0: No, 1: Yes) |

## 🧠 3. Training

Train the imitation learning model using the collected dataset:

```bash
python lerobot/scripts/train.py \
  dataset_repo_id=local_user/koch_test1 \
  policy=act_koch_real \
  env=koch_real \
  hydra.run.dir=outputs/train/act_koch_test \
  hydra.job.name=act_koch_test \
  device=cuda \
  wandb.enable=true
```

#### Parameter Explanation

| Parameter         | Description                            |
| ----------------- | -------------------------------------- |
| `dataset_repo_id` | Path to dataset                        |
| `policy`          | Training policy (e.g., ACT, diffusion) |
| `env`             | Environment name                       |
| `hydra.run.dir`   | Directory to store training results    |
| `hydra.job.name`  | Job name                               |
| `device`          | Training device (`cuda` / `cpu`)       |
| `wandb.enable`    | Enable experiment tracking             |

For single-objective tasks: 100 datasets .
For multi-objective tasks: combine multiple datasets for mixed training.



------

## 🧩 4. Inference (Deduction)

Evaluate model performance on new tasks:

```bash
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

#### Key Differences from Data Recording

- `-p`: Path to pretrained model checkpoint
- `--repo-id`: Use prefix `eval_` to indicate inference dataset

## 🍵 Example Task: Pouring Tea into a Cup



After training with ACT policy, the robot successfully performed a **tea-pouring** task, demonstrating stable grasping, fluid control, and accurate spatial coordination.