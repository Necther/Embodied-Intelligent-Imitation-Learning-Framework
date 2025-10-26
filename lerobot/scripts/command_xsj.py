# from lerobot.common.robot_devices.robots.manipulator import ManipulatorRobot
# from lerobot.common.robot_devices.cameras.opencv import OpenCVCamera

# robot = ManipulatorRobot(
#     leader_arms={"main": leader_arm},
#     follower_arms={"main": follower_arm},
#     calibration_dir=".cache/calibration/koch",
#     cameras={
#         "laptop": OpenCVCamera(4, fps=30, width=640, height=480),
#         "phone": OpenCVCamera(2, fps=30, width=640, height=480),
#     },
# )
# robot.connect()

from lerobot.common.robot_devices.motors.dynamixel import DynamixelMotorsBus

leader_port = "/dev/ttyACM2"
follower_port = "/dev/ttyACM1"

leader_arm = DynamixelMotorsBus(
    port=leader_port,
    motors={
        "shoulder_pan": (1, "xl330-m077"),
        "shoulder_lift": (2, "xl330-m077"),
        "elbow_flex": (3, "xl330-m077"),
        "wrist_flex": (4, "xl330-m077"),
        "wrist_roll": (5, "xl330-m077"),
        "gripper": (6, "xl330-m077"),
    },
)

follower_arm = DynamixelMotorsBus(
    port=follower_port,
    motors={
        "shoulder_pan": (1, "xl430-w250"),
        "shoulder_lift": (2, "xl430-w250"),
        "elbow_flex": (3, "xl330-m288"),
        "wrist_flex": (4, "xl330-m288"),
        "wrist_roll": (5, "xl330-m288"),
        "gripper": (6, "xl330-m288"),
    },
)

from lerobot.common.robot_devices.robots.manipulator import ManipulatorRobot

robot = ManipulatorRobot(
    robot_type="koch",
    leader_arms={"main": leader_arm},
    follower_arms={"main": follower_arm},
    calibration_dir=".cache/calibration/koch",
)

robot.connect()

#6个回车

leader_pos = robot.leader_arms["main"].read("Present_Position")
follower_pos = robot.follower_arms["main"].read("Present_Position")

print(leader_pos)
print(follower_pos)

# sudo chmod 666 /dev/ttyACM1



# python lerobot/scripts/control_robot.py record \
#   --robot-path lerobot/configs/robot/koch.yaml \
#   --fps 30 \
#   --repo-id local_user/koch_test1 \
#   --tags tutorial \
#   --warmup-time-s 5 \
#   --episode-time-s 15 \
#   --reset-time-s 5 \
#   --num-episodes 2 \
#   --push-to-hub 0

from lerobot.common.robot_devices.robots.manipulator import ManipulatorRobot
from lerobot.common.robot_devices.cameras.opencv import OpenCVCamera

robot = ManipulatorRobot(
    leader_arms={"main": leader_arm},
    follower_arms={"main": follower_arm},
    calibration_dir=".cache/calibration/koch",
    cameras={
        "laptop": OpenCVCamera(2, fps=30, width=640, height=480),
        "phone": OpenCVCamera(4, fps=30, width=640, height=480),
    },
)
robot.connect()

from lerobot.common.robot_devices.cameras.opencv import OpenCVCamera

camera = OpenCVCamera(camera_index=0)
camera.disconnect()


# 查询正在使用的摄像头
# lsof /dev/video*
# 杀死进程
# kill -9 <PID>



# python lerobot/scripts/control_robot.py record \
#   --robot-path lerobot/configs/robot/koch.yaml \
#   --fps 30 \
#   --repo-id local_user/koch_test2 \
#   --tags tutorial \
#   --warmup-time-s 5 \
#   --episode-time-s 15 \
#   --reset-time-s 5 \
#   --num-episodes 2 \
#   --push-to-hub 0


# /home/xsj/code/lerobot/data/local_user/koch_test_t

# python lerobot/scripts/train.py \
#   dataset_repo_id=data/local_user/koch_test_t \
#   policy=act_koch_real \
#   env=koch_real \
#   hydra.run.dir=outputs/train/act_koch_test \
#   hydra.job.name=act_koch_test \
#   device=cuda \
#   wandb.enable=true

# python lerobot/scripts/train.py
#     dataset_repo_id=/media/wwq/wwq/2024.12.20/Xbot/lerobot/data/ww12357i/koch1 \
#     policy=act_koch_real \ 
#     env=koch_real \
#     hydra.run.dir=outputs/train/act_koch_real \
#     hydra.job.name=act_koch_test \
#     device=cuda \
#     wandb.enable=false

# python lerobot/scripts/control_robot.py record   --robot-path lerobot/configs/robot/koch.yaml   --fps 30   --repo-id local_user/eval_koch2   --tags tutorial eval   --warmup-time-s 5   --episode-time-s 18   --reset-time-s 5   --num-episodes 10   --push-to-hub 0   -p outputs/train/act_koch_eraser/checkpoints/last/pretrained_model
