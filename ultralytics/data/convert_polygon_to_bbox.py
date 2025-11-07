import os
import glob

def convert_polygon_to_bbox(polygon_points):
    x_coords = [float(polygon_points[i]) for i in range(0, len(polygon_points), 2)]
    y_coords = [float(polygon_points[i]) for i in range(1, len(polygon_points), 2)]
    x_min = min(x_coords)
    x_max = max(x_coords)
    y_min = min(y_coords)
    y_max = max(y_coords)
    x_center = (x_min + x_max) / 2
    y_center = (y_min + y_max) / 2
    width = x_max - x_min
    height = y_max - y_min
    return x_center, y_center, width, height

# Paths
labels_folder = "/data/abbas/Data/blue_tear.yolov11/train/labels"  # e.g., /annotations/
output_folder = "/data/abbas/Data/blue_tear.yolov11/train/bbox"  # where new bbox files will be saved
os.makedirs(output_folder, exist_ok=True)

# Process each annotation file
for txt_file in glob.glob(os.path.join(labels_folder, "*.txt")):
    with open(txt_file, "r") as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        parts = line.strip().split()
        class_id = parts[0]
        polygon_coords = parts[1:]
        
        if len(polygon_coords) >= 6:  # polygon should have at least 3 points
            x_c, y_c, w, h = convert_polygon_to_bbox(polygon_coords)
            new_line = f"{class_id} {x_c:.6f} {y_c:.6f} {w:.6f} {h:.6f}\n"
            new_lines.append(new_line)
    
    # Save converted file
    output_file = os.path.join(output_folder, os.path.basename(txt_file))
    with open(output_file, "w") as f:
        f.writelines(new_lines)
