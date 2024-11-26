# Image Compression Script

A Python script to compress images to a target file size while preserving quality. This script is ideal for optimizing images for web uploads, saving storage space, or preparing images for online platforms.

## Features

- Compress images to a specified target size in KB.
- Supports `.png`, `.jpg`, and `.jpeg` formats.
- Automatically converts images to RGB mode for consistent compression.
- Batch processes multiple images in a directory.

## Prerequisites

- Python 3.x installed on your system.
- The `Pillow` library installed. Install it using:
  ```bash
  pip install pillow


Installation:-

Clone this repository:

git clone https://github.com/yourusername/image-compression-script.git

Navigate to the project directory:

cd image-compression-script





Usage:-

Place the images you want to compress in a directory.
Update the image_directory and output_directory variables in the script with the paths to your input and output directories.
Run the script:

 
python compress_images.py  OR python main.py

The compressed images will be saved in the specified output directory.


Example:-

Here’s an example of how to use the script in your Python code:

# Example usage in the script
image_directory = r'C:\images\input'
output_directory = r'C:\images\output'
process_images(image_directory, output_directory, target_size_kb=1024)


Contributing:-

Contributions are welcome! If you have ideas for improvements or new features, feel free to fork this repository, implement your changes, and submit a pull request.

License:-

This project is licensed under the MIT License - see the LICENSE file for details.




Happy Image Compressing

