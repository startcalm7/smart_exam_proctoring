import cv2
import os


def validate_video(video_path):
    """
    Validates video before processing.
    Returns (is_valid, message)
    """

    if not os.path.exists(video_path):
        return False, "Video file does not exist."

    if os.path.getsize(video_path) == 0:
        return False, "Video file is empty."

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return False, "Cannot open video file. Possibly corrupt."

    ret, frame = cap.read()

    if not ret:
        cap.release()
        return False, "Video contains no readable frames."

    # Check resolution
    height, width = frame.shape[:2]
    if height < 240 or width < 320:
        cap.release()
        return False, "Video resolution too low."

    # Check brightness (low light detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness = gray.mean()

    if brightness < 40:
        cap.release()
        return False, "Video too dark (low light condition)."

    cap.release()
    return True, "Video is valid."
