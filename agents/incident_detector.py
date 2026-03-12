def detect_incident(errors):

    if errors > 10:
        return "High error rate detected"
    elif errors > 5:
        return "Moderate incident"
    else:
        return "System stable"