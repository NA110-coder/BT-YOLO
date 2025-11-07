import os

# === CONFIG ===
mask_folder = "/data/abbas/U-Net/blue_tear/val_mask"  # change this for val/test if needed
suffix_to_remove = "_mask"

for filename in os.listdir(mask_folder):
    if filename.endswith('.jpg') and suffix_to_remove in filename:
        new_name = filename.replace(suffix_to_remove, "")
        src = os.path.join(mask_folder, filename)
        dst = os.path.join(mask_folder, new_name)
        os.rename(src, dst)
        print(f"Renamed: {filename} → {new_name}")
