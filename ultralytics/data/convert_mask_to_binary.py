import os
import cv2
import numpy as np

# === CONFIGURATION ===
input_mask_folder = '/data/abbas/Data/Blue_Tear/mask_binary/train/masks'       # <- Change this
output_mask_folder = '/data/abbas/Data/Blue_Tear/mask_binary/train/masks2'         # <- Change this (can be same as input if you want overwrite)
os.makedirs(output_mask_folder, exist_ok=True)

# === PROCESS ALL FILES ===
for filename in os.listdir(input_mask_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        in_path = os.path.join(input_mask_folder, filename)
        out_path = os.path.join(output_mask_folder, filename)

        # Load mask in grayscale
        mask = cv2.imread(in_path, cv2.IMREAD_GRAYSCALE)

        # Convert to binary (any non-zero becomes 255)
        binary_mask = np.where(mask > 0, 255, 0).astype(np.uint8)

        # Save binary mask
        cv2.imwrite(out_path, binary_mask)
        print(f"Converted: {filename}")
