import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("无法开启摄像头")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("无法获取帧，退出...")
        break

cv2.imshow('Camera Feed', frame)


cap.release()
cv2.destroyAllWindows()
