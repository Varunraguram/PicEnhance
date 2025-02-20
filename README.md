# Background Removal Script

This script removes the background from images in a specified folder using the `rembg` package. The processed images are saved in a separate output folder.

---

## Installation

Before running the script, ensure that you have Python installed. Then, install the required dependencies:

```sh
pip install rembg pillow
```

- `rembg`: Library used for background removal.
- `pillow`: Python Imaging Library (PIL) for image processing.

---

## How to Use the Script

1. **Set Up Image Folders:**
   - Place all input images in a folder (e.g., `C:/baw/PicEnhance/input`).
   - Ensure the output folder exists (e.g., `C:/baw/PicEnhance/output`).

2. **Run the Script:**
   - Save the script as `background_removal.py`.
   - Run it using:
     ```sh
     python background_removal.py
     ```

3. **Check the Output:**
   - Processed images (without backgrounds) will be saved in the output folder.

---

## Code Explanation (Line by Line)

```python
import os
import traceback
from rembg import remove
from PIL import Image
```
- **`os`**: Handles file and folder operations.
- **`traceback`**: Captures detailed error messages for debugging.
- **`rembg.remove`**: The function that removes the background from images.
- **`PIL.Image`**: Used to open and save image files.

```python
input_folder = "C:/baw/PicEnhance/input"
output_folder = "C:/baw/PicEnhance/output"
```
- **Defines the folder paths** where input images are stored and output images will be saved.

```python
os.makedirs(output_folder, exist_ok=True)
```
- **Creates the output folder** if it does not already exist.

```python
supported_formats = (".png", ".jpg", ".jpeg", ".bmp", ".webp", ".tiff")
```
- **Specifies supported image file formats** that the script will process.

```python
for file_name in os.listdir(input_folder):
```
- **Loops through each file** in the input folder.

```python
    input_path = os.path.join(input_folder, file_name)
    output_path = os.path.join(output_folder, file_name)
```
- **Constructs the full file paths** for input and output images.

```python
    if file_name.lower().endswith(supported_formats):
```
- **Checks if the file is an image** by verifying its extension.

```python
        try:
            with Image.open(input_path) as img:
                output_image = remove(img)
                output_image.save(output_path, format=img.format)
```
- **Opens the image using PIL**.
- **Removes the background using `remove(img)`**.
- **Saves the processed image** in the same format.

```python
            print(f"✅ Background removed for: {file_name}")
```
- **Displays a success message** for each processed image.

```python
        except Exception as e:
            print(f"❌ Error processing {file_name}: {e}")
            traceback.print_exc()
```
- **Handles errors gracefully** and prints detailed error messages.

```python
print("\n🎉 Background removal completed!")
```
- **Final message** indicating that the script has finished running.

---

## Additional Features
- Supports `.png`, `.jpg`, `.jpeg`, `.bmp`, `.webp`, and `.tiff` formats.
- Provides detailed error handling.
- Automatically creates the output folder if it does not exist.

---

## Troubleshooting
- If the script doesn't work, check that the images are in the correct input folder.
- Ensure that `rembg` and `pillow` are installed properly using `pip list`.
- If errors occur, check the traceback messages in the terminal.

---

## Future Enhancements
- Add a progress bar for better user experience.
- Allow users to specify custom input/output paths.
- Provide an option to resize images after background removal.

---

### 🎯 Now you are ready to remove backgrounds from your images efficiently! 🚀
###input image 

 
![Online Image](https://github.com/Varunraguram/PicEnhance/blob/main/PicEnhance/read-image/1.png)

![out image part 1](https://github.com/Varunraguram/PicEnhance/blob/main/PicEnhance/read-image/2.png)

![out image part 1](https://github.com/Varunraguram/PicEnhance/blob/main/PicEnhance/read-image/3.png)


![out image part 1](https://raw.githubusercontent.com/Varunraguram/PicEnhance/main/PicEnhance/read-image/4.png)




