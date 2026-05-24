# Image Segmentation – DSA Project

## Overview
This project implements an Image Segmentation System using concepts from Data Structures and Algorithms (DSA).  
The segmentation is performed through a mean-similarity–based region merging algorithm supported by the Disjoint Set Union (Union–Find) data structure.

Users can upload an image through the frontend, and the backend processes it to generate a clean and meaningful segmented output.

---

## Team Members — Group 31
- Manthan Nayak  
- Sai Swaroop Guntuku  
- Ankur Kumar 

---

## Objective
To segment an image into meaningful regions by grouping similar pixels and avoiding over-segmentation caused by noise, shadows, and natural variations in color.

---

## Key Idea
Traditional pixel-wise comparison often results in noisy or fragmented segmentation.  
To overcome this, the project focuses on region-level merging using:

- Mean color similarity  
- Spatial neighborhood information  
- Region-level comparison rather than pixel-level  

The merging process is efficiently handled using the Union–Find (DSU) structure.

---

## Tech Stack

### Backend
- Python  
- Flask  
- NumPy  
- OpenCV  
- DSU (Union–Find)

### Frontend
- HTML  
- CSS  
- JavaScript  

---

## Process
- Upload image through a simple UI  
- Region-based segmentation using a DSU merging algorithm  
- Displays:
  - Original Image  
  - Intermediate Region Merging  
  - Final Segmented Output  
- Clean and responsive design  

---

## How to Run the Project

### 1. Install Dependencies
```bash
pip install numpy opencv-python flask
```
### 2. Start the Flask Backend
```bash
python app.py
```

### 3. Open the Frontend
Open the main HTML file from the frontend folder in your browser and connect it to the running backend.

### 4. Viewing Output
After processing:
- The **Original Image** will appear first.
- The **Processed/Merged Image** will appear next.
- Finally, the **Segmented Output** will be displayed with distinct colors.


### Algorithm Summary

1. Extract pixel-level features:
   - Color information (R, G, B)
   - Spatial position (x, y)

2. Build edges between neighboring pixels:
   - 4-connectivity or 8-connectivity
   - Compute similarity between feature vectors

3. Initialize DSU (Disjoint Set Union):
   - Each pixel starts as its own set

4. Merge regions based on mean similarity:
   - Compare region means instead of individual pixels
   - Merge if similarity < threshold

5. Apply merging threshold to prevent over-merging:
   - Ensures objects do not collapse into one region

6. Generate final segmentation:
   - Assign unique labels to each region
   - Apply random/distinct colors for visualization

---

## Folder Structure
```
DSA-PROJECT/
│── app.py
│── main.py
│── Frontend/
│   │── index.html
│   │── script.js
│   │── styles.css
│── uploads/
│── output/
│── README.md
```
---

**Acknowledgements**

This work was developed as part of the DSA Course Project (Group 31).

**Conclusion**

By integrating DSA concepts such as Union–Find with image processing techniques, this project produces clean, efficient segmentation results. It demonstrates the power of algorithmic thinking in solving real-world problems.

Thank you for exploring our project!
