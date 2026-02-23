def update_streak(streak, detected, threshold):
    events = 0

    if detected:
        streak += 1
    else:
        if streak >= threshold:
            events += 1
        streak = 0

    return streak, events
