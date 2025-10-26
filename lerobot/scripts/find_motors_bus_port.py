# import time
# from pathlib import Path


# def find_available_ports():
#     ports = []
#     for path in Path("/dev").glob("tty*"):
#         ports.append(str(path))
#     return ports


# def find_port():
#     print("Finding all available ports for the MotorsBus.")
#     ports_before = find_available_ports()
#     print(ports_before)

#     print("Remove the usb cable from your MotorsBus and press Enter when done.")
#     input()

#     time.sleep(0.5)
#     ports_after = find_available_ports()
#     ports_diff = list(set(ports_before) - set(ports_after))

#     if len(ports_diff) == 1:
#         port = ports_diff[0]
#         print(f"The port of this MotorsBus is '{port}'")
#         print("Reconnect the usb cable.")
#     elif len(ports_diff) == 0:
#         raise OSError(f"Could not detect the port. No difference was found ({ports_diff}).")
#     else:
#         raise OSError(f"Could not detect the port. More than one port was found ({ports_diff}).")


# if __name__ == "__main__":
#     # Helper to find the usb port associated to all your MotorsBus.
#     find_port()
import time
from pathlib import Path


def find_available_ports():
    ports = []
    for path in Path("/dev").glob("tty*"):
        ports.append(str(path))
    return ports


def find_port():
    print("正在查找电机总线所有可用的端口。")
    ports_before = find_available_ports()
    print(ports_before)

    print("从电机总线上拔下 USB 线缆，完成后按回车键。")
    input()

    time.sleep(0.5)
    ports_after = find_available_ports()
    ports_diff = list(set(ports_before) - set(ports_after))

    if len(ports_diff) == 1:
        port = ports_diff[0]
        print(f"此电机总线的端口为 '{port}'")
        print("重新连接 USB 线缆。")
    elif len(ports_diff) == 0:
        raise OSError(f"无法检测到端口。未发现差异 ({ports_diff})。")
    else:
        raise OSError(f"无法检测到端口。发现了多个端口 ({ports_diff})。")


if __name__ == "__main__":
    # 用于查找与所有电机总线关联的 USB 端口的辅助工具。
    find_port()
