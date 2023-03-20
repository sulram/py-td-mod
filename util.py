def clamp(value, minimum, maximum):
    return max(min(value, maximum), minimum)

def mapped(value, start1, stop1, start2, stop2):
    mapped_value = (value - start1) * (stop2 - start2) / (stop1 - start1) + start2
    return mapped_value
