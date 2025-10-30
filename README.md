# TellMeTheTime - Analog Clock Reader

A computer vision project for reading time from analog clock images using edge detection and blob detection techniques.

## Project Structure

```
TellMeTheTime/
├── main.py                  # Main pipeline orchestrator
├── preprocessing.py         # Image preprocessing (blur, grayscale, etc.)
├── clock_detection.py       # Clock face detection using edge detection
├── blob_detection.py        # Blob detection for center and markers
├── hand_detection.py        # Clock hand detection using Hough Line Transform
├── time_calculation.py      # Convert angles to time
├── visualization.py         # Display and save results
├── clock.png               # Input clock image
└── requirements.txt        # Python dependencies
```

## Pipeline Overview

### 1. **Preprocessing** (`preprocessing.py`)
- Load and convert image to grayscale
- Apply Gaussian blur to reduce noise
- Histogram equalization for better contrast

### 2. **Clock Detection** (`clock_detection.py`) - **EDGE DETECTION**
- Canny edge detection
- Hough Circle Transform to detect clock face
- Localize clock region

### 3. **Blob Detection** (`blob_detection.py`) - **BLOB DETECTION**
- SimpleBlobDetector to find clock center pivot
- Detect hour markers as circular blobs
- Contour-based blob detection as alternative

### 4. **Hand Detection** (`hand_detection.py`) - **EDGE DETECTION**
- Morphological operations to enhance hands
- Hough Line Transform to detect hand lines
- Filter lines passing through center

### 5. **Time Calculation** (`time_calculation.py`)
- Calculate angles of hour and minute hands
- Convert angles to time values
- Validate and format the result

### 6. **Visualization** (`visualization.py`)
- Draw detection results (circles, blobs, lines)
- Display intermediate steps
- Save final annotated image

## Computer Vision Concepts Covered

### Edge Detection
- **Canny Edge Detector**: Finds edges in the image
- **Hough Circle Transform**: Detects circular shapes (clock face)
- **Hough Line Transform**: Detects straight lines (clock hands)

### Blob Detection
- **SimpleBlobDetector**: Detects blob-like structures
- **Contour Detection**: Alternative blob detection method
- **Blob Filtering**: Filter by area, circularity, and other properties

### Additional Techniques
- **Morphological Operations**: Enhance features (erosion, dilation)
- **Gaussian Blur**: Noise reduction
- **Histogram Equalization**: Contrast enhancement

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
2. Move to `clock_detection.py` - learn edge detection and Hough Circle Transform
3. Explore `blob_detection.py` - understand blob detection techniques
4. Study `hand_detection.py` - learn Hough Line Transform
5. Complete with `time_calculation.py` - convert geometry to time

## Next Steps

Each file contains function signatures with detailed comments explaining:
- What the function should do
- What parameters it takes
- What it should return

Your task is to implement these functions using OpenCV and NumPy!

## Resources

- [OpenCV Documentation](https://docs.opencv.org/)
- [Canny Edge Detection](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html)
- [Hough Transform](https://docs.opencv.org/4.x/d9/db0/tutorial_hough_lines.html)
- [Blob Detection](https://learnopencv.com/blob-detection-using-opencv-python-c/)
