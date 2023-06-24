import os
from PIL import Image
import png

def optimize_and_fix_png_files(folder_path):
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

                    try:
                        # Attempt to fix the PNG file only if it cannot be identified
                        with open(file_path, 'rb') as f:
                            png_data = png.Reader(file=f).read()

                        # Check if the PNG file has IDAT chunks
                        if png_data[2] is None:
                            raise png.FormatError("This PNG file has no IDAT chunks.")

                        # Retrieve the pixel data
                        pixels = list(png_data[2])

                        # Write the pixel data back to the file
                        with open(file_path, 'wb') as f:
                            png_writer = png.Writer(width=png_data[0], height=png_data[1], alpha=True)
                            png_writer.write(f, pixels)

                        print(f"Fixed: {filename}")
                    except Exception as e:
                        print(f"Error fixing {filename}: {str(e)}")

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
optimize_and_fix_png_files(folder_path)
