import os
from rembg import remove
from PIL import Image

# Input and output folder paths
input_folder = "C:/baw/PicEnhance/input"  # Replace with the path to your folder with images
output_folder = "C:/baw/PicEnhance/output"   # Replace with the path to save processed images

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each image in the input folder
for file_name in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file_name)
    output_path = os.path.join(output_folder, file_name)

    # Check if the file is an image
    if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
        try:
            with open(input_path, "rb") as input_file:
                input_image = input_file.read()
                output_image = remove(input_image)

            # Save the processed image
            with open(output_path, "wb") as output_file:
                output_file.write(output_image)

            print(f"Background removed for: {file_name}")
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

print("Background removal completed!")
