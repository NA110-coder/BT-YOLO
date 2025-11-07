import cv2
import matplotlib.pyplot as plt
import os

# Paths
image_path = '/data/abbas/Data/Blue_Tear/mask_binary/train/images/IMG-20241024-WA0005_jpg.rf.b0b9daa1c5919b852320ca01481dc902.jpg'
mask_path = '/data/abbas/Data/Blue_Tear/mask_binary/train/masks/IMG-20241024-WA0005_jpg.rf.b0b9daa1c5919b852320ca01481dc902_mask.jpg'

# Load image and mask
img = cv2.imread(image_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

# Optional: colorize mask for visualization
colored_mask = cv2.applyColorMap(mask, cv2.COLORMAP_JET)
overlay = cv2.addWeighted(img, 0.7, colored_mask, 0.3, 0)

# Show all
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(img)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Mask")
plt.imshow(mask, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Overlay")
plt.imshow(overlay)
plt.axis('off')

# Save the full figure
plt.savefig("/data/abbas/Data/Blue_Tear/mask_binary/overlay_check.jpg")
print("✅ Overlay image saved as: overlay_check.jpg")

