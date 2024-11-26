from PIL import Image
import os

def compress_image_to_size(image_path, output_path, target_size_kb=1024):
    with Image.open(image_path) as img:
        # Convert image to RGB if necessary
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        
        # Start with a high quality setting
        quality = 95
        while quality > 10:
            # Save the image with the current quality setting
            img.save(output_path, "JPEG", quality=quality, optimize=True)
            # Check the file size
            file_size_kb = os.path.getsize(output_path) / 1024
            if file_size_kb <= target_size_kb:
                break
            # Reduce quality for further compression
            quality -= 5

def process_images(directory, output_directory, target_size_kb=1024):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(directory):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(directory, filename)
            output_path = os.path.join(output_directory, filename)
            print(f"Compressing image: {filename}")
            compress_image_to_size(image_path, output_path, target_size_kb)
            print(f"Saved compressed image: {output_path}")

# Specify the directory containing your images and the output directory
image_directory = r'D:\adobe stock work\2\set_1_cleaned\done'
output_directory = r'D:\adobe stock work\2\set_1_cleaned\done\New folder'
process_images(image_directory, output_directory, target_size_kb=1024)