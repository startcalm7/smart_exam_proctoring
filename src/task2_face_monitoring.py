from ultralytics import YOLO

face_model = YOLO("yolov8n-face.pt")

def detect_faces(frame):
    results = face_model(frame, conf=0.2)
    face_count = sum(len(r.boxes) for r in results)
    return face_count
