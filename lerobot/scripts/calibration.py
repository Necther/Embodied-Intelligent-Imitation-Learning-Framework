from lerobot.common.robot_devices.motors.dynamixel import DynamixelMotorsBus
from lerobot.common.robot_devices.robots.manipulator import ManipulatorRobot
import numpy as np

def main():
# 定义电机端口
    leader_port = "/dev/ttyACM3"  # 替换为您的端口
    follower_port = "/dev/ttyACM2"  # 替换为您的端口

    # 创建领导电机臂
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

    # 创建跟随电机臂
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

    robot = ManipulatorRobot(
    robot_type="koch",
    leader_arms={"main": leader_arm},
    follower_arms={"main": follower_arm},
    calibration_dir=".cache/calibration/koch",
    )
    robot.connect()
    leader_pos = robot.leader_arms["main"].read("Present_Position")
    follower_pos = robot.follower_arms["main"].read("Present_Position")

    # 设置 NumPy 打印格式
    np.set_printoptions(suppress=True, precision=3, floatmode="fixed")
    
    print(leader_pos)
    print(follower_pos)

if __name__ == "__main__":
    main()
