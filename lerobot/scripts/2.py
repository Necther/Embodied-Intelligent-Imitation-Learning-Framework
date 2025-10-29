import cv2

def display_camera(camera_index):
    # 打开指定索引号的相机
    cap = cv2.VideoCapture(camera_index)

    # 检查相机是否成功打开
    if not cap.isOpened():
        print(f"无法打开相机索引 {camera_index}")
        return

    while True:
        # 从相机读取一帧画面
        ret, frame = cap.read()

        # 检查是否成功读取到画面
        if not ret:
            print("无法获取画面，退出。")
            break

        # 显示当前帧画面
        cv2.imshow(f"Camera {camera_index}", frame)

        # 按 'q' 键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放相机资源
    cap.release()
    # 关闭所有 OpenCV 窗口
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 这里设置相机索引号，通常 0 表示默认相机
    camera_index = 4
    display_camera(camera_index)
