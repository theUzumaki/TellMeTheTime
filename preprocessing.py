"""
Preprocessing module for clock image preparation.
Contains functions for image loading and initial processing.
"""

import cv2
import numpy as np


def apply_gaussian_blur(image, grayscale, bw, kernel_size=(5, 5)):
    """
    Apply Gaussian blur to reduce noise in the image.
    
    Args:
        image (numpy.ndarray): Input grayscale image
        kernel_size (tuple): Size of the Gaussian kernel (must be odd numbers)
    
    Returns:
        numpy.ndarray: Blurred image
    """
    return cv2.GaussianBlur(image, kernel_size, 0), cv2.GaussianBlur(grayscale, kernel_size, 0), cv2.GaussianBlur(bw, kernel_size, 0)


def apply_histogram_equalization(image):
    """
    Apply histogram equalization to improve contrast.
    Useful when the clock image has poor lighting conditions.
    
    Args:
        image (numpy.ndarray): Input grayscale image
    
    Returns:
        numpy.ndarray: Image with equalized histogram
    """
    return cv2.equalizeHist(image)


def preprocess_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    if image.ndim == 3 and image.shape[2] == 3:
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, bw_image = cv2.threshold(grayscale_image, 127, 255, cv2.THRESH_BINARY)

    # Abilitate if image needs more contrast
    # grayscale_image = apply_histogram_equalization(grayscale_image)

    return image, grayscale_image, bw_image