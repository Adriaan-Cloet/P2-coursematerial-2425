def overlapping_intervals(interval1, interval2):
    # Unpack bounds
    left1, right1 = interval1
    left2, right2 = interval2
    
    # Check if intervals are valid (left <= right)
    if left1 > right1 or left2 > right2:
        return False

    # Check if intervals overlap
    return left1 <= right2 and right1 >= left2