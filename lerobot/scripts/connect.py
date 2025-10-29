from lerobot.common.robot_devices.motors.dynamixel import DynamixelMotorsBus
import tqdm

# 定义电机端口
leader_port = "/dev/ttyACM3"  # 替换为您的端口
follower_port = "/dev/ttyACM2"  # 替换为您的端口

leader_arm = DynamixelMotorsBus(
    port=leader_port,
    motors={
        # name: (index, model)
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
        # name: (index, model)
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



seconds = 3000
frequency = 100
for _ in tqdm.tqdm(range(seconds*frequency)):
    leader_pos = robot.leader_arms["main"].read("Present_Position")
    robot.follower_arms["main"].write("Goal_Position", leader_pos)

