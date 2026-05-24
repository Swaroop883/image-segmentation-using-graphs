# Image Segmentation Using Graphs

## Overview
This project implements a Graph-Based Image Segmentation System using core concepts from Data Structures and Algorithms (DSA). 

Traditional pixel-wise comparison often results in noisy, fragmented, or overly sensitive segmentation. To overcome this, our system models the image as a mathematical graph and uses the **Disjoint Set Union (Union-Find)** data structure to perform  region-level merging. 

Users can upload an image through a clean web interface, and the Flask backend processes it to generate meaningful, cleanly segmented outputs.

---

## Team Members 
- Manthan Nayak  
- Sai Swaroop Guntuku  
- Ankur Kumar 

---

## Algorithms & Data Structures Used

This project implements two distinct mathematical approaches to region merging, both powered by a highly optimized **Union-Find (DSU)** architecture featuring *Path Compression* and *Union by Rank/Size*.

### 1. Mean-Similarity Merging
*   Groups pixels by calculating the running average color (Mean) of an entire region.
*   Before merging two adjacent regions, it calculates the Euclidean distance between their average colors.
*   If the distance falls below a dynamic threshold, the DSU merges them.

### 2. Felzenszwalb-Huttenlocher (FH) Algorithm
*   An advanced graph-based approach that adapts to natural textures and gradients.
*   Instead of averages, it tracks the **Internal Difference** (the maximum edge weight inside a segment).
*   It merges two regions only if the boundary difference between them is smaller than the internal texture of *both* regions, allowing smooth gradients (like skies) to segment cleanly without harsh banding.

---

## Tech Stack

**Backend:**
- Python  
- Flask (Server & API Routing)
- NumPy (High-performance matrix math)
- OpenCV (Image reading, scaling, and LAB color space conversion)

**Frontend:**
- HTML5  
- CSS3  
- Vanilla JavaScript  

---

## How to Run the Project

### 1. Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install numpy opencv-python Flask
```
---

### 2. Start the Flask Server

Navigate to the root directory of the project and start the backend:

```bash
python app.py
```

---

## 3. Open the App

Open your web browser and go to:

```text
http://127.0.0.1:5000
```

(Note: The Flask server automatically routes and serves the frontend HTML, no need to open the file manually).

---

## Processing Pipeline

### Feature Extraction

The image is converted from standard BGR to LAB Color Space to perfectly mimic human visual perception and eliminate shadow interference.

### Graph Construction

The image is mapped into a grid where pixels are nodes. Edges are built using 8-way connectivity, with weights calculated via 3D Euclidean distance.

### Sorting

Edges are sorted by weight ((O(E \log E))) to guarantee that the most similar pixels are evaluated first.

### DSU Merging

The Union-Find structure processes the edges, merging pixels based on either Mean Similarity or FH logic.

### Cleanup

A post-processing pass forces a union on any region that falls below the `min_size` threshold to eliminate noise and speckling.

### Visualization

The backend assigns random distinct colors or average segment colors and returns the generated image to the UI.

---

## Folder Structure

```text
DSA-PROJECT/
│── app.py                 # Flask server and API endpoints
│── main.py                # Core graph setup and image processing pipeline
│── segmentation/          # Custom Python package
│   ├── __init__.py
│   ├── color_utils.py     # Grayscale & LAB conversions
│   ├── edge_builder.py    # 8-connectivity graph constructor
│   └── union_find.py      # DSU architecture & merging algorithms
│── Frontend/
│   ├── index.html
│   ├── script.js
│   └── styles.css
│── uploads/               # Auto-generated (Stores user inputs)
│── outputs/               # Auto-generated (Stores segmented results)
└── README.md
```

---

## Acknowledgements

This work was developed as part of the DSA Course Project.

---

## Conclusion

By integrating core Data Structures (Union-Find) with advanced mathematical heuristics (FH Algorithm, LAB Color Space), this project produces clean, efficient segmentation results. It demonstrates the immense power of algorithmic thinking in solving complex, real-world computer vision problems.

Thank you for exploring our project!
