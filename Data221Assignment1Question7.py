def secondsSinceMidnight(seconds):
    if seconds < 0 or seconds >= 86400:
        return "invalid input"

    # Convert total seconds to hours
    hours = seconds // 3600

    # Convert remaining seconds to minutes
    minutes = (seconds % 3600) // 60

    # Get the remaining seconds after hours and minutes
    remainingSeconds = seconds % 60

    # Determine AM or PM
    if hours >= 12:
        period = "PM"
    else:
        period = "AM"

    hours = hours % 12
    if hours == 0:
        hours = 12
    return f"{hours}:{minutes:02d}:{remainingSeconds:02d}:{period}"
print(secondsSinceMidnight(80000))
