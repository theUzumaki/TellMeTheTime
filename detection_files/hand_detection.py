"""
Clock hand detection module using edge detection and line detection.
Detects hour and minute hands using Hough Line Transform.
"""

import numpy as np


def filter_lines_by_center(lines, center, max_distance_from_center=30, min_angle_difference=15):
    """
    Filter detected lines to keep only those passing through clock center.
    Clock hands should intersect at or near the center point.
    
    Args:
        lines (numpy.ndarray): Array of detected lines
        center (tuple): (x, y) center of the clock
        max_distance_from_center (int): Maximum allowed distance from center
        min_angle_difference (float): Minimum angle difference in degrees between distinct lines
    
    Returns:
        list: Filtered lines that pass through the center
    """
    filtered_lines = []
    cx, cy = center
    
    def get_line_angle(line):
        """Calculate the angle of a line from the center."""
        x1, y1, x2, y2 = line
        # Determine which endpoint is farther from center
        dist1 = np.hypot(x1 - cx, y1 - cy)
        dist2 = np.hypot(x2 - cx, y2 - cy)
        if dist1 < dist2:
            dx, dy = x2 - cx, cy - y2
        else:
            dx, dy = x1 - cx, cy - y1
        angle = np.degrees(np.arctan2(dx, dy))
        return (angle + 360) % 360
    
    for line in lines:
        x1, y1, x2, y2 = line

        dist1 = np.hypot(x1 - cx, y1 - cy)
        dist2 = np.hypot(x2 - cx, y2 - cy)

        if dist1 < max_distance_from_center or dist2 < max_distance_from_center:

            # Check if the line is too close to already chosen ones
            too_close = False
            current_angle = get_line_angle(line)
            
            for chosen_line in filtered_lines:
                chosen_angle = get_line_angle(chosen_line)
                chosen_x1, chosen_y1, chosen_x2, chosen_y2 = chosen_line
                
                # Calculate the minimum angular difference (accounting for wraparound)
                angle_diff = abs(current_angle - chosen_angle)
                angle_diff = min(angle_diff, 360 - angle_diff)
                
                # Calculate average distance between line endpoints
                # Check all possible endpoint pairings since lines can be in any order
                dist_avg_1 = (np.hypot(x1 - chosen_x1, y1 - chosen_y1) + 
                             np.hypot(x2 - chosen_x2, y2 - chosen_y2)) / 2
                dist_avg_2 = (np.hypot(x1 - chosen_x2, y1 - chosen_y2) + 
                             np.hypot(x2 - chosen_x1, y2 - chosen_y1)) / 2
                min_avg_dist = min(dist_avg_1, dist_avg_2)
                
                # Lines are too close if they have similar angles OR are spatially close
                if angle_diff < min_angle_difference or min_avg_dist < max_distance_from_center:
                    too_close = True
                    break
            
            if not too_close:
                filtered_lines.append(line)
        
        if len(filtered_lines) >= 2:
            break  # We only need two lines (hour and minute hands)
    return filtered_lines


def calculate_line_angle(line, center):
    """
    Calculate the angle of a line with respect to 12 o'clock position (vertical up).
    Angle is measured clockwise from 12 o'clock (0 degrees at top).
    
    Args:
        line (tuple): (x1, y1, x2, y2) line coordinates
        center (tuple): (x, y) center of the clock
    
    Returns:
        float: Angle in degrees (0-360), where 0 is 12 o'clock
    """
    
    x1, y1, x2, y2 = line
    cx, cy = center
    
    # Determine which endpoint is closer to the center
    dist1 = np.hypot(x1 - cx, y1 - cy)
    dist2 = np.hypot(x2 - cx, y2 - cy)
    if dist1 < dist2:
        x_end, y_end = x2, y2
    else:
        x_end, y_end = x1, y1
    
    # Calculate angle
    delta_x = x_end - cx
    delta_y = cy - y_end  # Invert y-axis for image coordinates
    angle_rad = np.arctan2(delta_x, delta_y)
    angle_deg = np.degrees(angle_rad)
    
    # Convert to clockwise angle from 12 o'clock
    angle_clockwise = (angle_deg + 360) % 360
    return angle_clockwise


def calculate_lines_length(lines):
    """
    Calculate the Euclidean length of a line.
    
    Args:
        line (tuple): (x1, y1, x2, y2) line coordinates
    
    Returns:
        float: Length of the line
    """

    markers = []
    for line in lines:
        x1, y1, x2, y2 = line
        length = np.hypot(x2 - x1, y2 - y1)
        markers.append((line, length))
    return markers


def identify_hour_and_minute_hands(lines, center):
    """
    Distinguish between hour and minute hands based on length and thickness.
    Typically, minute hand is longer than hour hand.
    
    Args:
        lines (list): List of detected lines passing through center
        center (tuple): (x, y) center of the clock
    
    Returns:
        tuple: (hour_hand_line, minute_hand_line) or (None, None) if not found
    """
    
    filtered_lines = filter_lines_by_center(lines, center)

    if not filtered_lines:
        return None, None
    
    # Calculate lengths of filtered lines
    markers_lengths = calculate_lines_length(filtered_lines)

    # Sort lines by length (longest first)
    markers_lengths.sort(key=lambda x: x[1], reverse=True)
    
    # Check if we have at least 2 lines
    if len(markers_lengths) == 1:
        return (markers_lengths[0][0], markers_lengths[0][0])  # Only one hand detected
    elif len(markers_lengths) == 0:
        return (None, None)  # No hands detected
    
    return (markers_lengths[1][0], markers_lengths[0][0])  # (hour_hand, minute_hand)

def read_time_from_hands(hour_hand_line, minute_hand_line, center):
    """
    Calculate the time indicated by the hour and minute hands.
    
    Args:
        hour_hand_line (tuple): (x1, y1, x2, y2) coordinates of hour hand line
        minute_hand_line (tuple): (x1, y1, x2, y2) coordinates of minute hand line
        center (tuple): (x, y) coordinates of clock center

    Returns:
        str: Detected time in format "HH:MM" or None if detection failed
    """

    hour_angle = calculate_line_angle(hour_hand_line, center)
    minute_angle = calculate_line_angle(minute_hand_line, center)

    # Map angles to clock time
    hour = int((hour_angle / 360) * 12) % 12
    minute = int((minute_angle / 360) * 60) % 60

    return f"{hour:02}:{minute:02}"