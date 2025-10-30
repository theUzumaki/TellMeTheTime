# TellMeTheTime - Analog Clock Reader

A computer vision project for reading time from analog clock images using edge detection and blob detection techniques.

## Project Structure

```
TellMeTheTime/
├── main.py                     # Main pipeline orchestrator
├── preprocessing.py            # Image preprocessing (blur, grayscale, etc.)
├── logger.py                   # Logging utilities for pipeline steps
├── detection_files/            # Detection modules
│   ├── hough_detection.py      # Clock face and line detection using Hough Transform
│   ├── blob_detection.py       # Blob detection for clock center
│   └── hand_detection.py       # Clock hand identification and time reading
├── processed_imgs/             # Output directory for processed images
├── clock_1.png                 # Sample clock image 1
├── clock_2.jpg                 # Sample clock image 2
├── requirements.txt            # Python dependencies
├── LICENSE                     # Project license
├── LOGGER_README.md           # Documentation for logging utilities
└── README.md                   # This file
```

## Pipeline Overview

### 1. **Preprocessing** (`preprocessing.py`)
- Load and convert image to grayscale
- Apply Gaussian blur to reduce noise
- Thresholding for better contrast

### 2. **Clock Detection** (`detection_files/hough_detection.py`) - **HOUGH TRANSFORM**
- Canny edge detection
- Hough Circle Transform to detect clock face
- Hough Line Transform to detect lines passing through center
- Localize clock region

### 3. **Blob Detection** (`detection_files/blob_detection.py`) - **BLOB DETECTION**
- SimpleBlobDetector to find clock center pivot
- Detect circular blobs for clock center identification

### 4. **Hand Detection** (`detection_files/hand_detection.py`) - **TIME READING**
- Identify hour and minute hands from detected lines
- Calculate angles and convert to time
- Read time from hands based on their positions

### 5. **Logging** (`logger.py`)
- Log pipeline steps and progress
- Track detection results
- Save processing information

## Computer Vision Concepts Covered

### Hough Transform
- **Canny Edge Detector**: Finds edges in the image
- **Hough Circle Transform**: Detects circular shapes (clock face)
- **Hough Line Transform**: Detects straight lines (clock hands)

### Blob Detection
- **SimpleBlobDetector**: Detects blob-like structures
- **Blob Filtering**: Filter by area, circularity, and other properties

### Additional Techniques
- **Gaussian Blur**: Noise reduction
- **Thresholding**: Binary image conversion
- **Geometric Calculations**: Angle computation for time reading

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
python main.py
```

## Learning Path

1. Start with `preprocessing.py` - understand image preparation
2. Move to `detection_files/hough_detection.py` - learn Hough Circle and Line Transform
3. Explore `detection_files/blob_detection.py` - understand blob detection techniques
4. Study `detection_files/hand_detection.py` - learn time reading from geometric calculations
5. Review `logger.py` - understand pipeline logging and tracking

## Implementation Details

Each module contains functions with detailed documentation explaining:
- What the function should do
- What parameters it takes
- What it should return
- Example usage patterns

## Resources

- [OpenCV Documentation](https://docs.opencv.org/)
- [Canny Edge Detection](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html)
- [Hough Transform](https://docs.opencv.org/4.x/d9/db0/tutorial_hough_lines.html)
- [Blob Detection](https://learnopencv.com/blob-detection-using-opencv-python-c/)
