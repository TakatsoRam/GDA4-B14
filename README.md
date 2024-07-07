# GDA4-B14
# 3D Model Visualization Application

## Description
This application is a simple 3D model viewer using Python, PyOpenGL, and PyGame. It allows you to view and manipulate three different 3D models: a cube, a triangular pyramid, and a triangular prism.

## Requirements
- Python 3.x
- PyOpenGL
- PyGame

## Installation
1. Install the necessary libraries using pip:
    ```
    pip install PyOpenGL PyOpenGL_accelerate pygame
    ```
2. Place `Cube.py`, `Pyramid.py`, `Prism.py`, and `Display.py` in the same directory.

## Usage
1. Run the `Display.py` script
2. Use the following keys to switch between models:
    - Press ‘1’ to view the Cube.
    - Press `2` to view the Pyramid.
    - Press ‘3’ to view the Prism.

3.Use these keys to translate the models:
    - Press ‘A’ to translate left along the x-axis.
    - Press ‘D’ to translate right along the x-axis.
    - Press ‘W’ to translate up along the y-axis.
    - Press ‘S’ to translate down along the y-axis.
    - Press ‘Q’ to translate forward along the z-axis.
    - Press ‘E’ to translate backward along the z-axis.

4 Use these keys to rotate the models:
    - Press ‘I’ to rotate up along the x-axis.
    - Press ‘K’ to rotate down along the x-axis.
    - Press ‘J’ to rotate left along the y-axis.
    - Press ‘L’ to rotate right along the y-axis.
    - Press ‘U’ to rotate left along the z-axis.
    - Press ‘O’ to rotate right along the z-axis.

5. Use these keys to scale the models:
    - Press ‘Z’ to shrink along the x-axis.
    - Press ‘X’ to grow along the x-axis.
    - Press ‘C’ to shrink along the y-axis.
    - Press ‘V’ to grow along the y-axis.
    - Press ‘B’ to shrink along the z-axis.
    - Press ‘N’ to grow along the z-axis.

## Files
- Cube.py: Contains the vertex and edge information for the cub.
- Pyramid.py: Contains the vertex and edge information for the pyramid.
- Prism.py: Contains the vertex and edge information for the prism.
- Display.py: Main script used to run the OpenGL application.
- `README.md`: This README file.

