# 360-Degree Object Tracking and Laser Targeting System

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![YOLO](https://img.shields.io/badge/YOLO-Object%20Detection-orange.svg)
![Computer Vision](https://img.shields.io/badge/Computer%20Vision-Stitching%20%26%20Tracking-green.svg)

An automated mechatronic system that combines a rotating camera and laser structure with advanced computer vision (YOLO) to scan environments, stitch panoramic images, detect objects, and precisely target them with a laser.

---

## 🚀 Overview

This project features a mechatronic system where a camera and a laser are mounted on a custom rotating structure. The system automatically pans across user-defined angles, captures multiple overlapping images, and stitches them into a comprehensive panoramic view. Using a **YOLO** object detection model, the system identifies target objects within the environment, calculates their coordinates, and autonomously aligns the hardware to mark them with a laser.

---

## ⚙️ Working Principle

1. **Scanning & Image Stitching:** 
   * The user defines the target observation area.
   * The rotating structure pans the camera across multiple angles to capture a series of sequential images.
   * Individual photos are algorithmically stitched together to create a single, high-resolution panorama of the entire area.

2. **Object Detection:** 
   * A **YOLO (You Only Look Once)** object detection model processes the stitched panoramic image.
   * The model accurately identifies, classifies, and records the exact locations of specified target objects.

3. **Targeting & Laser Marking:** 
   * Once the target coordinates are resolved, the system calculates the required rotation angles.
   * The rotating mechanism precisely aligns the camera and laser module with the selected objects, marking them automatically.

---

## 🛠️ Technologies & Components

* **Programming Language:** Python
* **Computer Vision & AI:** YOLO model, Image Stitching algorithms, OpenCV
* **Hardware / Mechanics:** Rotating structure, Camera module, Laser module
* **Control System:** Automated path calculation and hardware synchronization

---

## 📺 Demo

| Structure | Working Video Demo |
| :---: | :---: |
| ![Image](<img width="432" height="412" alt="image" src="https://github.com/user-attachments/assets/5cac4a31-b9b9-4008-87cf-4dbd4f93a03a" />) | ![Video Demo]([assets/demo_preview.gif](https://github.com/KeremCikikci/360ObjectDetection-marking/assets/98697826/dfb02741-992f-4851-bfd7-1ea080ee7a19))


