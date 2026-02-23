def calculate_risk(total_frames, face_violations,
                   person_violations, phone_events, book_events):

    # -------------------------------
    # 1️⃣ Severity Weights
    # -------------------------------
    WEIGHTS = {
        "face_violation": 2,
        "person_violation": 15,
        "phone": 50,   # Very serious cheating
        "book": 20
    }

    # -------------------------------
    # 2️⃣ Weighted Risk Score
    # -------------------------------
    risk_score = (
        face_violations * WEIGHTS["face_violation"] +
        person_violations * WEIGHTS["person_violation"] +
        phone_events * WEIGHTS["phone"] +
        book_events * WEIGHTS["book"]
    )

    # -------------------------------
    # 3️⃣ Risk Percentage (for display)
    # -------------------------------
    if total_frames > 0:
        risk_percentage = round((risk_score / total_frames) * 100, 2)
    else:
        risk_percentage = 0

    # -------------------------------
    # 4️⃣ SEVERITY OVERRIDE LOGIC
    # -------------------------------

    # Phone detected → Always HIGH
    if phone_events >= 1:
        risk_level = "HIGH"

    # Multiple persons → HIGH
    elif person_violations >= 1:
        risk_level = "HIGH"

    # Book detected → MODERATE
    elif book_events >= 1:
        risk_level = "MODERATE"

    # Fallback to percentage-based logic
    elif risk_percentage >= 50:
        risk_level = "CRITICAL"

    elif risk_percentage >= 25:
        risk_level = "HIGH"

    elif risk_percentage >= 10:
        risk_level = "MODERATE"

    else:
        risk_level = "LOW"

    return risk_score, risk_percentage, risk_level
