import json
from collections import defaultdict

def coco_to_vgg(coco_json_path, output_vgg_json_path, class_mapping):
    """
    Convert COCO segmentation format to VGG Image Annotator (VIA) format with proper class names.

    :param coco_json_path: Path to the input COCO JSON file.
    :param output_vgg_json_path: Path to the output VGG JSON file.
    :param class_mapping: Dictionary mapping category_id to class names (e.g., {1: 'blue_tear'}).
    """
    # Load COCO JSON
    with open(coco_json_path, 'r') as f:
        coco_data = json.load(f)

    # Initialize the VGG format dictionary
    vgg_data = {}

    # Create a mapping of image_id to image metadata
    image_id_to_metadata = {img['id']: img for img in coco_data['images']}

    # Group annotations by image_id
    annotations_by_image = defaultdict(list)
    for annotation in coco_data['annotations']:
        annotations_by_image[annotation['image_id']].append(annotation)

    # Process each image
    for image_id, annotations in annotations_by_image.items():
        # Get image metadata
        image_metadata = image_id_to_metadata[image_id]
        filename = image_metadata['file_name']
        size = image_metadata.get('width', 0) * image_metadata.get('height', 0)  # Approximate size

        # Regions for this image
        regions = {}
        for idx, annotation in enumerate(annotations):
            # Extract segmentation points
            segmentation = annotation['segmentation'][0]  # Assuming single polygon per object
            all_points_x = segmentation[0::2]  # Even indices for x-coordinates
            all_points_y = segmentation[1::2]  # Odd indices for y-coordinates

            # Add region with proper class name
            class_id = annotation['category_id']
            class_name = class_mapping.get(class_id, "unknown")  # Default to "unknown" if class_id not in mapping

            regions[str(idx)] = {
                "shape_attributes": {
                    "name": "polygon",
                    "all_points_x": all_points_x,
                    "all_points_y": all_points_y
                },
                "region_attributes": {
                    "class": class_name
                }
            }

        # Add to VGG data
        vgg_data[filename] = {
            "filename": filename,
            "size": size,
            "regions": regions
        }

    # Save the VGG JSON
    with open(output_vgg_json_path, 'w') as f:
        json.dump(vgg_data, f, indent=4)

    print(f"Converted COCO JSON to VGG JSON format and saved to {output_vgg_json_path}")


# Example usage
coco_json_path = "/data/abbas/Mask-R-CNN/roboflow_json/train.json"  # Replace with your COCO JSON file
output_vgg_json_path = "/data/abbas/Mask-R-CNN/vgg_json/train.json"  # Desired output path for VGG JSON
class_mapping = {1: "blue_tear"}  # Mapping COCO category_id to class names

coco_to_vgg(coco_json_path, output_vgg_json_path, class_mapping)
