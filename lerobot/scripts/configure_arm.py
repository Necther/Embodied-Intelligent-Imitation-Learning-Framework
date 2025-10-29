from lerobot.common.robot_devices.motors.dynamixel import DynamixelMotorsBus
from lerobot.common.robot_devices.motors.dynamixel import TorqueMode


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

    # 连接主机械臂
    try:
        leader_arm.connect()
        print("主机械臂连接成功。")
    except Exception as e:
        print(f"连接主机械臂时出错: {e}")

    # 连接从机械臂
    try:
        follower_arm.connect()
        print("从机械臂连接成功。")
    except Exception as e:
        print(f"连接从机械臂时出错: {e}")

    leader_pos = leader_arm.read("Present_Position")
    follower_pos = follower_arm.read("Present_Position")
    print(leader_pos)
    print(follower_pos)

    # follower_arm.write("Torque_Enable", TorqueMode.ENABLED.value)

    # # Get the current position
    # position = follower_arm.read("Present_Position")

    # # Update first motor (shoulder_pan) position by +10 steps
    # position[0] += 10
    # follower_arm.write("Goal_Position", position)

    # # Update all motors position by -30 steps
    # position -= 30
    # follower_arm.write("Goal_Position", position)

    # # Update gripper by +30 steps
    # position[-1] += 30
    # follower_arm.write("Goal_Position", position[-1], "gripper")

    follower_arm.write("Torque_Enable", TorqueMode.DISABLED.value)
    leader_arm.write("Torque_Enable", TorqueMode.DISABLED.value)

if __name__ == "__main__":
    main()
