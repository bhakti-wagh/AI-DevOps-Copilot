def analyze_logs(file_path):

    errors = 0
    warnings = 0

    with open(file_path) as file:
        for line in file:

            if "ERROR" in line:
                errors += 1

            if "WARNING" in line:
                warnings += 1

    return {
        "errors": errors,
        "warnings": warnings
    }