from lerobot.common.robot_devices.motors.dynamixel import DynamixelMotorsBus
from lerobot.common.robot_devices.robots.manipulator import ManipulatorRobot
import numpy as np

import yaml


def main():
# 定义电机端口

    with open("koch.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    leader_port = config['leader_arms']['main']['port']  # 替换为您的端口
    follower_port = config['follower_arms']['main']['port']  # 替换为您的端口

   
     # 创建领导电机臂
    leader_arm = DynamixelMotorsBus(
        port=leader_port,
        motors= config['leader_arms']['main']['motors']
    )

    # 创建跟随电机臂
    follower_arm = DynamixelMotorsBus(
        port=follower_port,
        motors= config['follower_arms']['main']['motors']
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
