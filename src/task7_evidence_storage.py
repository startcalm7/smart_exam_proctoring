import os
import cv2
from datetime import datetime

BASE_EVIDENCE_DIR = "static/evidence"

def save_evidence(frame, violation_type, frame_number):

    folder_path = os.path.join(BASE_EVIDENCE_DIR, violation_type)
    os.makedirs(folder_path, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{violation_type}_frame_{frame_number}_{timestamp}.jpg"
    filepath = os.path.join(folder_path, filename)

    cv2.imwrite(filepath, frame)

    return filepath
