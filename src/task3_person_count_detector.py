def count_persons(detections, model):
    person_count = 0
    for box in detections.boxes:
        cls = int(box.cls[0])
        label = model.names[cls]
        if label == "person":
            person_count += 1
    return person_count
