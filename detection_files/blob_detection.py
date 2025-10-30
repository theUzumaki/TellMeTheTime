"""
Blob detection module for identifying clock features.
Detects the clock center pivot and hour markers using blob detection.
"""

import cv2
import numpy as np


def setup_blob_detector():
    """
    Create and configure a SimpleBlobDetector with appropriate parameters.
    Configure parameters to detect circular blobs (clock center, hour markers).
    
    Returns:
        cv2.SimpleBlobDetector: Configured blob detector
    """
    
    params = cv2.SimpleBlobDetector_Params()

    # Set Area filtering parameters
    params.filterByArea = True
    params.minArea = 100000
    params.maxArea = 50000000  # Set a large maximum area limit

    # Set Circularity filtering parameters
    params.filterByCircularity = True
    params.minCircularity = 0.2

    # Set Convexity filtering parameters
    params.filterByConvexity = False

    # Set Inertia filtering parameters
    params.filterByInertia = False

    detector = cv2.SimpleBlobDetector_create(params)
    return detector


def detect_clock_center_blob(image, approximate_center):
    """
    Detect the center pivot point of the clock using blob detection.
    The center is typically a circular blob where hands are attached.
    
    Args:
        image (numpy.ndarray): Preprocessed grayscale image
        approximate_center (tuple): (x, y) approximate center from circle detection
    
    Returns:
        tuple: (x, y) precise center coordinates, or None if not found
    """
    
    detector = setup_blob_detector()
    keypoints = detector.detect(image)

    if not keypoints:
        return None, None

    # Find the blob closest to the approximate center
    min_distance = float('inf')
    clock_center = None

    # Check the number of channels in the image
    if len(image.shape) == 3 and image.shape[2] == 3:
        # Convert to grayscale if the image is in color
        blob_image = image.copy()
    elif len(image.shape) == 2:
        # Convert grayscale or binary image to BGR for color drawing
        blob_image = cv2.cvtColor(image.copy(), cv2.COLOR_GRAY2BGR)

    # Draw edge predicted center
    cv2.circle(blob_image, (approximate_center[0][0], approximate_center[0][1]), 15, (255, 0, 0), -1)  # Draw in blue

    for keypoint in keypoints:
        kp_x, kp_y = keypoint.pt
        distance = np.sqrt((kp_x - approximate_center[0][0])**2 + (kp_y - approximate_center[0][1])**2)

        if distance < min_distance:
            min_distance = distance
            clock_center = (int(kp_x), int(kp_y), int(keypoint.size / 2))  # (x, y, radius)
            
        cv2.circle(blob_image, (int(kp_x), int(kp_y)), int(keypoint.size / 2), (0, 0, 255), 2)  # Draw in red

    cv2.circle(blob_image, (clock_center[0], clock_center[1]), clock_center[2], (0, 255, 0), 4)  # Draw in green

    return clock_center, blob_image


def detect_hour_markers(image, center, radius):
    """
    Detect hour markers on the clock face using blob detection.
    Hour markers are often circular dots or numbers.
    
    Args:
        image (numpy.ndarray): Preprocessed grayscale image
        center (tuple): (x, y) center of the clock
        radius (int): Radius of the clock face
    
    Returns:
        list: List of (x, y) coordinates of detected hour markers
    """
    pass


def find_contours_as_blobs(image):
    """
    Alternative blob detection using contour detection.
    Find blob-like structures by detecting and filtering contours.
    
    Args:
        image (numpy.ndarray): Binary or grayscale image
    
    Returns:
        list: List of contours representing blob-like structures
    """
    pass


def filter_blobs_by_properties(blobs, min_area=None, max_area=None, circularity_threshold=0.7):
    """
    Filter detected blobs based on area and circularity properties.
    
    Args:
        blobs (list): List of detected blobs/contours
        min_area (float): Minimum area of blob
        max_area (float): Maximum area of blob
        circularity_threshold (float): Minimum circularity (0-1)
    
    Returns:
        list: Filtered list of blobs
    """
    pass
