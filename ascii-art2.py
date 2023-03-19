import os
import numpy as np
import PIL.Image
import tempfile
import shutil

# Define the ASCII characters to use, ordered by decreasing brightness.
ASCII_CHARS = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

def resize_image(image, new_width=100):
    """Resizes the image to the specified width and adjusts the height accordingly."""
    width, height = image.size
    new_height = int(new_width * height / width)
    return image.resize((new_width, new_height))

def image_to_ascii(image, width=100):
    """Converts the image to ASCII art."""
    image = resize_image(image, new_width=width)
    pixels = np.array(image.convert('L')) # Convert the image to grayscale
    pixel_range = 256 / len(ASCII_CHARS)
    ascii_chars = np.array([ASCII_CHARS[min(int(pixel / pixel_range), len(ASCII_CHARS)-1)] for pixel in pixels.flatten()])
    return '\n'.join([''.join(row) for row in ascii_chars.reshape(pixels.shape).tolist()])

# Get the input filename from the user
input_filename = input('Enter the path to the input image: ')

# Load the image from the input file
try:
    image = PIL.Image.open(input_filename)
except FileNotFoundError:
    print('Error: Input file not found')
    exit()

# Convert the image to ASCII art
ascii_art = image_to_ascii(image)

# Write the ASCII art to a temporary file
with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    f.write(ascii_art)

# Copy the temporary file to the output file location
output_filename = input('Enter the path to save the output ASCII art: ')
shutil.copy(f.name, output_filename)

# Delete the temporary file
if f.name:
    os.unlink(f.name)

# Print a success message
print('ASCII art saved to', output_filename)
