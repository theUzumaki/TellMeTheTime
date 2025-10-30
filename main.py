"""
Main pipeline for clock time reading.
Orchestrates all modules to detect and read time from a clock image.
"""

import os
import cv2
import numpy as np

# Import preprocessing utilities
from preprocessing import preprocess_image, apply_gaussian_blur

# Import detection modules
from detection_files.hough_detection import detect_clock_circle, detect_lines_hough
from detection_files.blob_detection import detect_clock_center_blob
from detection_files.hand_detection import identify_hour_and_minute_hands, read_time_from_hands

# Import logging utilities
from logger import (
    log_section_header,
    log_step,
    log_error,
    log_file_saved,
    log_detection_result,
    log_application_title,
    log_final_result
)


def read_clock_time(image_path, visualize=True, save_output=False):
    """
    Complete pipeline to read time from a clock image.
    
    Pipeline Steps:
        1. Preprocess the image (grayscale, blur, threshold)
        2. Detect edges using Canny edge detection
        3. Detect clock face using Hough Circle Transform
        4. Detect clock center using blob detection
        5. Detect hour markers using Hough Line Transform
        6. Identify clock hands and calculate time
    
    Args:
        image_path (str): Path to the clock image
        visualize (bool): Whether to display intermediate results (default: True)
        save_output (bool): Whether to save the result image (default: False)
    
    Returns:
        str: Detected time in format "HH:MM", or None if detection failed
    """
    # Setup output directory for processed images
    processed_imgs_dir = "processed_imgs"
    os.makedirs(processed_imgs_dir, exist_ok=True)
    
    log_section_header("CLOCK TIME DETECTION PIPELINE")
    
    # ========== STEP 1: IMAGE PREPROCESSING ==========
    log_step(1, 6, "Image Preprocessing")
    
    # Convert to grayscale and apply thresholding
    original_image, grayscale_image, bw_image = preprocess_image(image_path)
    original_image, grayscale_image, bw_image = apply_gaussian_blur(
        original_image, grayscale_image, bw_image
    )

    if grayscale_image is None or bw_image is None:
        log_error("Image preprocessing failed", indentation_tabs=1, newline_after=1)
        return None
    
    # Save blurred image for debugging
    blurred_path = f"{processed_imgs_dir}/blurred_image.png"
    cv2.imwrite(blurred_path, grayscale_image)
    log_file_saved(blurred_path)
    
    # ========== STEP 2: EDGE DETECTION ==========
    log_step(2, 6, "Edge Detection")
    
    # Apply Canny edge detection
    edges = cv2.Canny(bw_image, 100, 200)

    if edges is None:
        log_error("Edge detection failed", indentation_tabs=1, newline_after=1)
        return None

    # Save edge detection result
    edges_path = f"{processed_imgs_dir}/edges.png"
    cv2.imwrite(edges_path, edges)
    log_file_saved(edges_path)

    # ========== STEP 3: CLOCK FACE DETECTION ==========
    log_step(3, 6, "Clock Face Detection (Hough Circle Transform)")
    
    # Detect clock circle using Hough Circle Transform
    clock = detect_clock_circle(grayscale_image)
    if clock is None:
        log_error("Clock face detection failed", indentation_tabs=1, newline_after=1)
        return None

    log_detection_result(
        "Clock center (edge-based)",
        f"{int(clock[0][0])} - {int(clock[0][1])}, radius: {int(clock[1])}"
    )

    # ========== STEP 4: CLOCK CENTER REFINEMENT ==========
    log_step(4, 6, "Clock Center Detection (Blob Detection)")
    
    # Refine clock center using blob detection
    clock, blob_image = detect_clock_center_blob(grayscale_image, clock)
    if clock is None:
        log_error("Clock center detection failed", indentation_tabs=1, newline_after=1)
        return None

    # Extract clock parameters
    clock_center = (int(clock[0]), int(clock[1]))
    clock_radius = int(clock[2])
    
    # Save blob detection visualization
    blob_image_path = f"{processed_imgs_dir}/clock_center_blobs.png"
    cv2.imwrite(blob_image_path, blob_image)
    log_file_saved(blob_image_path)
    log_detection_result(
        "Clock center (blob-based)",
        f"{clock_center[0]} - {clock_center[1]}, radius: {clock_radius}"
    )

    # ========== STEP 5: CLOCK HAND DETECTION ==========
    log_step(5, 6, "Hour Marker Detection (Hough Line Transform)")
    
    # Detect lines using Hough Line Transform
    lines = detect_lines_hough(edges)

    if lines is None or len(lines) == 0:
        log_error("No plausible markers detected", indentation_tabs=1, newline_after=1)
        return None
    
    # Visualize all detected lines (red)
    line_image = original_image.copy()
    for line in lines:
        x1, y1, x2, y2 = line
        cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imwrite(f"{processed_imgs_dir}/detected_lines.png", line_image)

    # Identify hour and minute hands from detected lines
    hour_markers = identify_hour_and_minute_hands(lines, clock_center)
    if hour_markers is None or hour_markers[0] is None or hour_markers[1] is None:
        log_error("Hour marker detection failed", indentation_tabs=1, newline_after=1)
        return None

    # Log and visualize identified clock hands (green)
    log_detection_result(
        "Hour markers positions",
        ", ".join([f"({int(x1)},{int(y1)})-({int(x2)},{int(y2)})" 
                  for (x1, y1, x2, y2) in hour_markers])
    )
    
    for marker in hour_markers:
        x1, y1, x2, y2 = marker
        cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)
    cv2.imwrite(f"{processed_imgs_dir}/detected_lines.png", line_image)

    # ========== STEP 6: TIME CALCULATION ==========
    log_step(6, 6, "Clock Hands Detection and Time Calculation")

    # Calculate time from hand angles
    estimated_time = read_time_from_hands(hour_markers[0], hour_markers[1], clock_center)
    
    if estimated_time:
        log_detection_result("Estimated Time", estimated_time)
        return estimated_time
    else:
        log_error("Time estimation failed", indentation_tabs=1, newline_after=1)
        return None



def main():
    """Main entry point for the clock time detection application."""
    IMAGE_PATH = "clock_2.jpg"
    
    log_application_title("CLOCK TIME DETECTION APPLICATION")
    
    # Run the complete detection pipeline
    detected_time = read_clock_time(IMAGE_PATH, visualize=True, save_output=True)
    
    # Display final results
    if detected_time:
        log_final_result(True, f"DETECTED TIME: {detected_time}")
    else:
        log_final_result(False, "Failed to detect time from the clock image")


if __name__ == "__main__":
    main()