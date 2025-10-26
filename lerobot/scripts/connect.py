from lerobot.common.robot_devices.motors.dynamixel import DynamixelMotorsBus
import tqdm

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

