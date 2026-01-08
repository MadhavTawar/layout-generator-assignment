"""
Building Layout Generator - 3 Different Densities
==================================================
Install: pip install matplotlib
Run: python layout_generator.py

Generates 3 layouts: Low density, Medium density, High density
"""

import matplotlib.pyplot as plt
import random

# Site size
SITE_W = 200
SITE_H = 140
PLAZA_SIZE = 40

def generate_layout(num_attempts):
    """Generate one layout by trying to place buildings"""
    
    # Plaza in middle
    plaza_x = SITE_W/2 - PLAZA_SIZE/2
    plaza_y = SITE_H/2 - PLAZA_SIZE/2
    
    buildings = []
    
    # Try to place buildings
    for i in range(num_attempts):
        
        # Pick random type: A or B
        if random.random() < 0.5:
            type = 'A'
            w = 30  # Tower A is 30x20
            h = 20
            color = 'blue'
        else:
            type = 'B'
            w = 20  # Tower B is 20x20
            h = 20
            color = 'green'
        
        # Pick random position
        x = random.uniform(10, SITE_W - w - 10)
        y = random.uniform(10, SITE_H - h - 10)
        
        # Check: Does it hit the plaza?
        hits_plaza = not (x + w < plaza_x or x > plaza_x + PLAZA_SIZE or 
                          y + h < plaza_y or y > plaza_y + PLAZA_SIZE)
        
        if hits_plaza:
            continue
        
        # Check: Too close to other buildings?
        too_close = False
        for other in buildings:
            ox, oy, ow, oh = other[0], other[1], other[2], other[3]
            
            gap_x = max(x - (ox + ow), ox - (x + w), 0)
            gap_y = max(y - (oy + oh), oy - (y + h), 0)
            distance = (gap_x**2 + gap_y**2)**0.5
            
            if distance < 15:
                too_close = True
                break
        
        if too_close:
            continue
        
        # All good! Add building
        buildings.append([x, y, w, h, type, color])
    
    return buildings, plaza_x, plaza_y


def draw_layout(buildings, plaza_x, plaza_y, subplot_num, title):
    """Draw one layout"""
    
    plt.subplot(1, 3, subplot_num)
    
    # Draw site (gray box)
    plt.gca().add_patch(plt.Rectangle((0, 0), SITE_W, SITE_H, 
                                      fill=False, edgecolor='black', linewidth=2))
    
    # Draw plaza (yellow box)
    plt.gca().add_patch(plt.Rectangle((plaza_x, plaza_y), PLAZA_SIZE, PLAZA_SIZE, 
                                      facecolor='yellow', edgecolor='orange', linewidth=2))
    plt.text(plaza_x + PLAZA_SIZE/2, plaza_y + PLAZA_SIZE/2, 'PLAZA', 
             ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Draw each building
    for building in buildings:
        x, y, w, h, type, color = building
        
        plt.gca().add_patch(plt.Rectangle((x, y), w, h, 
                                          facecolor=color, edgecolor='black', alpha=0.7))
        
        plt.text(x + w/2, y + h/2, type, 
                 ha='center', va='center', color='white', fontsize=9, fontweight='bold')
    
    # Count buildings
    count_a = sum(1 for b in buildings if b[4] == 'A')
    count_b = sum(1 for b in buildings if b[4] == 'B')
    total_area = count_a*30*20 + count_b*20*20
    
    # Setup plot
    plt.xlim(0, SITE_W)
    plt.ylim(0, SITE_H)
    plt.gca().set_aspect('equal')
    plt.grid(True, alpha=0.3)
    plt.xlabel('meters', fontsize=9)
    plt.ylabel('meters', fontsize=9)
    plt.title(f'{title}\nA:{count_a} | B:{count_b} | Total:{len(buildings)} | Area:{total_area}m²', 
              fontsize=10, fontweight='bold')
    
    return count_a, count_b, total_area


# Main program
print("\n" + "="*60)
print("BUILDING LAYOUT GENERATOR - 3 DENSITIES")
print("="*60)

plt.figure(figsize=(18, 6))

# Layout 1: LOW DENSITY (try 30 buildings)
print("\nGenerating Layout 1: LOW DENSITY...")
buildings1, px1, py1 = generate_layout(30)
count_a1, count_b1, area1 = draw_layout(buildings1, px1, py1, 1, "Layout 1: LOW DENSITY")
print(f"  Tower A: {count_a1} | Tower B: {count_b1} | Total: {len(buildings1)} | Area: {area1}m²")

# Layout 2: MEDIUM DENSITY (try 50 buildings)
print("\nGenerating Layout 2: MEDIUM DENSITY...")
buildings2, px2, py2 = generate_layout(50)
count_a2, count_b2, area2 = draw_layout(buildings2, px2, py2, 2, "Layout 2: MEDIUM DENSITY")
print(f"  Tower A: {count_a2} | Tower B: {count_b2} | Total: {len(buildings2)} | Area: {area2}m²")

# Layout 3: HIGH DENSITY (try 80 buildings)
print("\nGenerating Layout 3: HIGH DENSITY...")
buildings3, px3, py3 = generate_layout(80)
count_a3, count_b3, area3 = draw_layout(buildings3, px3, py3, 3, "Layout 3: HIGH DENSITY")
print(f"  Tower A: {count_a3} | Tower B: {count_b3} | Total: {len(buildings3)} | Area: {area3}m²")

print("\n" + "="*60)
print("Legend: Blue=Tower A (30x20m) | Green=Tower B (20x20m)")
print("="*60)

plt.suptitle('Building Layout Generator - 3 Different Cardinalities (Densities)', 
             fontsize=14, fontweight='bold')
plt.tight_layout()

print("\nClose the window to exit.")
plt.show()