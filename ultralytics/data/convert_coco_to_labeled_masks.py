import json
import numpy as np
import skimage.draw
import cv2
import os
import shutil

def create_mask(image_info, annotations, output_folder):
    # Create an empty mask as a numpy array
    mask_np = np.zeros((image_info['height'], image_info['width']), dtype=np.uint8)

    # Counter for the object number
    object_number = 1

    for ann in annotations:
        if ann['image_id'] == image_info['id']:
            # Extract segmentation polygon
            for seg in ann['segmentation']:
                if len(seg) < 6:  # Skip invalid polygons
                    continue
                rr, cc = skimage.draw.polygon(np.array(seg[1::2]), np.array(seg[0::2]), mask_np.shape)
                mask_np[rr, cc] = object_number
                object_number += 1  # Assign unique label to each object

    # Save mask as JPG using OpenCV
    mask_filename = image_info['file_name'].replace('.jpg', '_mask.jpg')
    mask_path = os.path.join(output_folder, mask_filename)
    cv2.imwrite(mask_path, mask_np)

    print(f"Saved mask for {image_info['file_name']} to {mask_path}")

def main(json_file, mask_output_folder, image_output_folder, original_image_dir):
    # Load COCO JSON annotations
    with open(json_file, 'r') as f:
        data = json.load(f)

    images = data['images']
    annotations = data['annotations']

    # Ensure the output directories exist
    os.makedirs(mask_output_folder, exist_ok=True)
    os.makedirs(image_output_folder, exist_ok=True)

    for img in images:
        # Create the masks
        create_mask(img, annotations, mask_output_folder)
        
        # Copy original image
        original_image_path = os.path.join(original_image_dir, img['file_name'])
        new_image_path = os.path.join(image_output_folder, os.path.basename(original_image_path))
        shutil.copy2(original_image_path, new_image_path)
        print(f"Copied original image to {new_image_path}")

if __name__ == '__main__':
    original_image_dir = '/data/abbas/Data/Blue_Tear/coco_json/train'
    json_file = '/data/abbas/Data/Blue_Tear/coco_json/train/_annotations.coco.json'
    mask_output_folder = '/data/abbas/Data/Blue_Tear/mask_binary/train/masks'
    image_output_folder = '/data/abbas/Data/Blue_Tear/mask_binary/train/images'
    main(json_file, mask_output_folder, image_output_folder, original_image_dir)
