#!/usr/bin/env python


"""Capture video feed from a camera as raw images."""

import argparse
import datetime as dt
from pathlib import Path

import cv2


def display_and_save_video_stream(output_dir: Path, fps: int, width: int, height: int):
    now = dt.datetime.now()
    capture_dir = output_dir / f"{now:%Y-%m-%d}" / f"{now:%H-%M-%S}"
    if not capture_dir.exists():
        capture_dir.mkdir(parents=True, exist_ok=True)

    # Opens the default webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    cap.set(cv2.CAP_PROP_FPS, fps)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    frame_index = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow("Video Stream", frame)
        cv2.imwrite(str(capture_dir / f"frame_{frame_index:06d}.png"), frame)
        frame_index += 1

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the capture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs/cam_capture/"),
        help="Directory where the capture images are written. A subfolder named with the current date & time will be created inside it for each capture.",
    )
    parser.add_argument(
        "--fps",
        type=int,
        default=30,
        help="Frames Per Second of the capture.",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=1280,
        help="Width of the captured images.",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=720,
        help="Height of the captured images.",
    )
    args = parser.parse_args()
    display_and_save_video_stream(**vars(args))
