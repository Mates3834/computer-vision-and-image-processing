# Computer Vision and Image Processing

A collection of graduate-level computer vision and image processing studies covering **image enhancement, segmentation, object analysis, image representation, and object detection**.

The project explores fundamental computer vision techniques and their implementation for extracting and analyzing information from digital images.

---

## Overview

The repository covers several areas of classical computer vision:

- Image preprocessing
- Histogram analysis
- Histogram equalization
- Image segmentation
- Binary image analysis
- Object area estimation
- Centroid detection
- Bounding-box extraction
- Object orientation
- Horizontal and vertical projections
- Run-Length Encoding (RLE)
- Haar Cascade based face detection

---

## 1. Image Enhancement

Grayscale image characteristics are investigated using intensity histograms.

### Histogram Analysis

Image intensity distributions are calculated and visualized to analyze the distribution of grayscale values.

### Histogram Equalization

Histogram equalization is applied to improve image contrast and redistribute intensity values.

The original and enhanced images can then be compared in terms of their intensity distributions.

---

## 2. Image Segmentation

Threshold-based segmentation is used to separate objects from the background.

The processing pipeline can be summarized as:

```text
Input Image
     ↓
Grayscale Conversion
     ↓
Histogram Analysis
     ↓
Thresholding
     ↓
Binary Image
     ↓
Object Analysis
```

---

## 3. Object Analysis

Following segmentation, several geometric properties of the detected object are extracted.

These include:

- Object area
- Centroid
- Bounding box
- Orientation

The resulting features provide a basic geometric representation of objects within binary images.

---

## 4. Image Projection

Horizontal and vertical projections are investigated as compact representations of object structure.

```text
Binary Image
    │
    ├──► Horizontal Projection
    │
    └──► Vertical Projection
```

Projection profiles provide information about the spatial distribution of object pixels along the image axes.

---

## 5. Run-Length Encoding

Run-Length Encoding (RLE) is investigated as a simple image representation and compression technique.

The workflow consists of:

```text
Binary Image
     ↓
RLE Encoding
     ↓
Encoded Representation
     ↓
RLE Decoding
     ↓
Reconstructed Image
```

The reconstructed image can be compared with the original binary image to verify the encoding and decoding process.

---

## 6. ALOI Image Analysis

Object images from the **ALOI dataset** are used in image-processing experiments.

The analysis includes:

- Binary image generation
- Horizontal projections
- Vertical projections
- RLE representation
- Image reconstruction

Multiple object groups and test images are used to evaluate the processing pipeline.

---

## 7. Haar Cascade Face Detection

A separate computer vision study investigates **Haar Cascade based face detection**.

The project compares face-detection behavior using:

- Camera images
- Static photographs

The study also investigates practical limitations affecting detection performance.

These include:

- Illumination
- Viewing angle
- Background complexity
- Facial expressions
- Variations in facial appearance
- Real-time computational requirements

---

## Computer Vision Pipeline

The studies collectively demonstrate a classical computer vision workflow:

```text
             Image Acquisition
                    ↓
              Preprocessing
                    ↓
          Image Enhancement
                    ↓
              Segmentation
                    ↓
             Feature Extraction
                    ↓
        Object / Face Detection
                    ↓
                Analysis
```

---

## Technologies

- MATLAB
- Image Processing
- Computer Vision
- Image Segmentation
- Feature Extraction
- Haar Cascade
- Run-Length Encoding
- ALOI Dataset

---

## Research Areas

- Computer Vision
- Image Processing
- Object Detection
- Pattern Recognition
- Image Segmentation
- Feature Extraction
- Autonomous Perception

---

## Repository Structure

```text
computer-vision-and-image-processing/
│
├── README.md
│
├── image-enhancement/
│   ├── histogram/
│   └── histogram-equalization/
│
├── segmentation/
│   └── thresholding/
│
├── object-analysis/
│   ├── area/
│   ├── centroid/
│   ├── bounding-box/
│   └── orientation/
│
├── image-representation/
│   ├── projections/
│   └── rle/
│
├── face-detection/
│   └── haar-cascade/
│
├── results/
│
└── docs/
```

---

## Project Status

This repository consolidates graduate-level studies developed in **Computer Vision in Control and Automation Systems**.

The repository is structured as a technical portfolio demonstrating fundamental image-processing and computer-vision methods.
