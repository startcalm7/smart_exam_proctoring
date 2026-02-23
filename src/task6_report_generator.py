def generate_report(mode, total_frames,
                    face_violations, person_violations,
                    phone_events, book_events,
                    risk_score, risk_percentage, risk_level):

    return {
        "mode": mode,
        "total_frames": total_frames,
        "face_violations": face_violations,
        "person_violations": person_violations,
        "phone_events": phone_events,
        "book_events": book_events,
        "risk_score": risk_score,
        "risk_percentage": risk_percentage,
        "risk_level": risk_level
    }
