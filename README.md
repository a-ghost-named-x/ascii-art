# Image to ASCII Art Converter

This Python script, ascii-art.py, allows you to transform images into creative ASCII art using the PIL (Pillow) library for image manipulation and NumPy for efficient array operations.

## Features

- Resizes input images to a specified width while maintaining the aspect ratio
- Converts images to grayscale
- Maps grayscale pixel values to ASCII characters based on brightness
- Saves the generated ASCII art to a user-specified output file

## Dependencies

To run the script, you will need the following Python libraries:

- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/installation.html)
- [NumPy](https://numpy.org/install/)

-## Usage

1. Run the script in your Python environment:
2. Enter the path to the input image file when prompted:
3. Enter the path where you want to save the output ASCII art file:
4. The script will process the input image, create the ASCII art, and save it to the specified output file.

## Design

The script is designed with the following functions:

- `resize_image(image, new_width=100)`: Resizes the image to the specified width and adjusts the height accordingly to maintain the aspect ratio.
- `image_to_ascii(image, width=100)`: Converts the image to ASCII art by first resizing the image, converting it to grayscale, and then mapping each pixel to an ASCII character based on its brightness.

The script uses the following global variable to define the ASCII characters used for the art:

- `ASCII_CHARS`: A list of ASCII characters ordered by decreasing brightness.

The main part of the script consists of:

1. Taking input from the user for the input image file path and output file path.
2. Loading the input image using the PIL library.
3. Converting the image to ASCII art using the `image_to_ascii()` function.
4. Writing the generated ASCII art to a temporary file.
5. Copying the temporary file to the specified output file location.
6. Deleting the temporary file.
7. Printing a success message.

## Contributing

Feel free to submit pull requests or report issues to help improve the script or add new features.
