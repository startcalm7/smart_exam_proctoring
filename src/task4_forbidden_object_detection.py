def detect_forbidden_objects(detections, model):
    phone_detected = False
    book_detected = False

    for box in detections.boxes:
        cls = int(box.cls[0])
        label = model.names[cls]

        if label == "cell phone":
            phone_detected = True
        elif label == "book":
            book_detected = True

    return phone_detected, book_detected
