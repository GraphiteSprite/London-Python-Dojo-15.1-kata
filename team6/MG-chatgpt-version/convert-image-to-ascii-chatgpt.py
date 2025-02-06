import numpy as np
from PIL import Image

# List of ASCII characters ordered by increasing brightness (dark to light)
ASCII_CHARS = ["@", "#", "8", "&", "o", ":", "*", ".", " "]


# Function to map pixel intensity to ASCII characters
def pixel_to_ascii(r, g, b):
    # Convert the RGB values to grayscale using the luminance formula
    gray_value = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # Map the grayscale value to an ASCII character
    ascii_char = ASCII_CHARS[int(gray_value / 255 * (len(ASCII_CHARS) - 1))]
    return ascii_char


# Function to convert an image to ASCII
def image_to_ascii(image_path, new_width=100, new_height=50):
    image = Image.open(image_path)
    image = image.resize((new_width, new_height))  # Resize the image to the desired dimensions
    pixels = np.array(image)

    ascii_image = ""

    for row in pixels:
        for pixel in row:
            r, g, b = pixel[:3]  # Extract RGB values
            ascii_image += f'<span style="color: rgb({r},{g},{b})">{pixel_to_ascii(r, g, b)}</span>'
        ascii_image += "<br>"

    return ascii_image


# Display the coloured ASCII art
from IPython.display import display, HTML


def display_ascii(image_path, new_width=100, new_height=50):
    ascii_art = image_to_ascii(image_path, new_width, new_height)
    display(HTML(f"<div style='font-family: monospace; white-space: pre-wrap;'>{ascii_art}</div>"))

# Usage example:
# display_ascii("path_to_image.jpg", 100, 50)