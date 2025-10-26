from lerobot.common.robot_devices.motors.dynamixel import DynamixelMotorsBus
from lerobot.common.robot_devices.motors.dynamixel import TorqueMode


def main():

    with open("koch.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    leader_port = config['leader_arms']['main']['port']  # 替换为您的端口
    follower_port = config['follower_arms']['main']['port']  # 替换为您的端口


    leader_arm = DynamixelMotorsBus(
        port=leader_port,
        motors= config['leader_arms']['main']['motors']
    )

    # 创建跟随电机臂
    follower_arm = DynamixelMotorsBus(
        port=follower_port,
        motors= config['follower_arms']['main']['motors']
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
