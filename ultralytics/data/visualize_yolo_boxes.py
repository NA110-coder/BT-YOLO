import cv2
import os
import glob

# ----- Step 1: Paths Setup -----
images_folder = "/data/abbas/yoloSAM/yolov13/images_contrast"             # 🔁 Change this: Original image folder
labels_folder = "/data/abbas/yoloSAM/yolov13/images_txt"   # 🔁 Change this: Converted .txt (YOLO bbox) folder
output_folder = "/data/abbas/images_with_boxes"      # 🔁 Change this: Where to save annotated images
os.makedirs(output_folder, exist_ok=True)

# Image extension (use .jpg or .png as per your data)
image_ext = ".jpg"

# ----- Step 2: Loop Through Images -----
for image_path in glob.glob(os.path.join(images_folder, f"*{image_ext}")):
    filename = os.path.splitext(os.path.basename(image_path))[0]
    label_path = os.path.join(labels_folder, f"{filename}.txt")
    output_path = os.path.join(output_folder, f"{filename}_bbox.jpg")

    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # Draw boxes if annotation file exists
    if os.path.exists(label_path):
        with open(label_path, "r") as f:
            lines = f.readlines()

        for line in lines:
            parts = line.strip().split()
            class_id = parts[0]
            x_center = float(parts[1]) * width
            y_center = float(parts[2]) * height
            box_width = float(parts[3]) * width
            box_height = float(parts[4]) * height

            x1 = int(x_center - box_width / 2)
            y1 = int(y_center - box_height / 2)
            x2 = int(x_center + box_width / 2)
            y2 = int(y_center + box_height / 2)

            # Draw rectangle and class label
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, f'{class_id}', (x1, y1 - 8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save output image with bounding boxes
    cv2.imwrite(output_path, image)

print("✅ All images saved with bounding boxes in:", output_folder)

