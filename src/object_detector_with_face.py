import cv2
import os
from ultralytics import YOLO

from src.task2_face_monitoring import detect_faces
from src.task3_person_count_detector import count_persons
from src.task4_forbidden_object_detection import detect_forbidden_objects
from src.task5_behavior_logic import update_streak
from src.task6_report_generator import generate_report
from src.task8_risk_analytics import calculate_risk
from src.task7_evidence_storage import save_evidence
from src.task9_error_handler import validate_video


def run_detection(video_path, mode="CLASSROOM"):

    # ===============================
    # TASK 9: VIDEO VALIDATION
    # ===============================
    is_valid, message = validate_video(video_path)
    if not is_valid:
        return {
            "mode": mode,
            "error": message
        }

    try:
        object_model = YOLO("yolov8n.pt")
    except Exception as e:
        return {
            "mode": mode,
            "error": f"YOLO model loading failed: {str(e)}"
        }

    cap = cv2.VideoCapture(video_path)

    total_frames = 0
    face_violations = 0
    person_violations = 0
    phone_events = 0
    book_events = 0

    phone_streak = 0
    book_streak = 0
    STREAK_THRESHOLD = 15

    evidence_paths = []

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            total_frames += 1

            try:
                obj_results = object_model(frame, conf=0.25)[0]
            except Exception:
                continue  # Skip faulty frame safely

            person_count = count_persons(obj_results, object_model)
            phone_detected, book_detected = detect_forbidden_objects(obj_results, object_model)
            face_count = detect_faces(frame)

            # ===============================
            # PERSON LOGIC (Classroom Mode)
            # ===============================
            if mode == "CLASSROOM" and person_count == 0:
                person_violations += 1
                path = save_evidence(frame, "person_missing", total_frames)
                evidence_paths.append(path)

            # ===============================
            # FACE LOGIC
            # ===============================
            if face_count is None or face_count == 0:
                face_violations += 1
                path = save_evidence(frame, "face_missing", total_frames)
                evidence_paths.append(path)

            # ===============================
            # PHONE STREAK LOGIC
            # ===============================
            phone_streak, new_phone_event = update_streak(
                phone_streak, phone_detected, STREAK_THRESHOLD
            )

            if new_phone_event > 0:
                phone_events += 1
                path = save_evidence(frame, "phone", total_frames)
                evidence_paths.append(path)

            # ===============================
            # BOOK STREAK LOGIC
            # ===============================
            book_streak, new_book_event = update_streak(
                book_streak, book_detected, STREAK_THRESHOLD
            )

            if new_book_event > 0:
                book_events += 1
                path = save_evidence(frame, "book", total_frames)
                evidence_paths.append(path)

    except Exception as e:
        cap.release()
        return {
            "mode": mode,
            "error": f"Processing error: {str(e)}"
        }

    cap.release()

    # ===============================
    # FINAL RISK CALCULATION
    # ===============================
    risk_score, risk_percentage, risk_level = calculate_risk(
        total_frames,
        face_violations,
        person_violations,
        phone_events,
        book_events
    )

    report = generate_report(
        mode,
        total_frames,
        face_violations,
        person_violations,
        phone_events,
        book_events,
        risk_score,
        risk_percentage,
        risk_level
    )

    report["evidence"] = evidence_paths

    return report
