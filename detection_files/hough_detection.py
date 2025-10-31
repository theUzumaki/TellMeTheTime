import cv2
import numpy as np

def detect_clock_circle(image):
    """
    Use Hough Circle Transform to detect the circular clock face.
    This is an edge-based detection method.
    
    Args:
        image (numpy.ndarray): Original grayscale image
    
    Returns:
        tuple: (x, y, radius) of the detected clock circle, or None if not found
    """

    low_res_image = cv2.pyrDown(image)
    circles = cv2.HoughCircles(low_res_image, cv2.HOUGH_GRADIENT, dp=1, minDist=100,
                                      param1=100, param2=30,
                                      minRadius=30, maxRadius=0)

    if circles is not None:
        circles = np.uint16(np.around(circles))

        # Assuming the first detected circle is the clock
        x, y, radius = circles[0][0]

        # Scale back to original image size
        x *= 2
        y *= 2
        radius *= 2

        return ((x, y), radius)
    else:
        return None

def detect_lines_hough(edges, min_line_length=80, max_line_gap=15):
    """
    Detect straight lines using Probabilistic Hough Line Transform.
    This will detect the clock hands as lines.
    
    Args:
        edges (numpy.ndarray): Edge-detected binary image
        min_line_length (int): Minimum length of a line
        max_line_gap (int): Maximum gap between line segments
    
    Returns:
        numpy.ndarray: Array of detected lines [(x1, y1, x2, y2), ...]
    """
    
    lines = cv2.HoughLinesP(edges, 
                            rho=1, 
                            theta=np.pi / 180, 
                            threshold=40, 
                            minLineLength=min_line_length, 
                            maxLineGap=max_line_gap)
    if lines is not None:
        return lines.reshape(-1, 4)  # Reshape to (N, 4)
    else:
        return []