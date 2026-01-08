# Layout Generator Assignment

This project is a Python-based layout generator that automatically creates
valid building layouts for a rectangular site while following spatial and
geometric constraints.

## Problem Overview
- Site Size: 200 m × 140 m
- Tower A: 30 m × 20 m
- Tower B: 20 m × 20 m
- Central Plaza: 40 m × 40 m (no construction zone)

The program ensures:
- Minimum distance between buildings
- Boundary offset from site edges
- Neighbor mix rule between Tower A and Tower B

## Output
- Visual layout generated using Matplotlib
- PDF report explaining logic, rules, and results

## How to Run
1. Install dependency:
   pip install matplotlib
2. Run the script:
   python layout_generator.py

## Tools Used
- Python
- Matplotlib
