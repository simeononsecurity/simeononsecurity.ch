import os
from PIL import Image
import png

def optimize_png_files(folder_path):
    # Iterate over all files and subfolders in the folder
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Check if the file is a PNG
            if filename.lower().endswith('.png'):
                try:
                    # Optimize the PNG file
                    optimize_png(file_path)

                    print(f"Optimized: {filename}")
                except Exception as e:
                    print(f"Error optimizing {filename}: {str(e)}")

def optimize_png(file_path):
    try:
        # Open the image using PIL
        image = Image.open(file_path)

        # Convert the image to a palette image with a limited color palette
        quantized_image = image.quantize(colors=256, method=2, dither=Image.NONE)

        # Remove metadata
        quantized_image.save(file_path, optimize=True, pnginfo=image.info)

    except Exception as e:
        raise e

# Specify the folder path where the PNG files are located
folder_path = r""

# Call the function to optimize and attempt fixing PNG files in the folder and its subfolders
optimize_png_files(folder_path)
