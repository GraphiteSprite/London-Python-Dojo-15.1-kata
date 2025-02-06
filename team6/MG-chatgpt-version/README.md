// Link to chatgpt prompt history:

// https://chatgpt.com/share/67a3cd5a-f7a8-8013-b585-7b9fd372ccd6

# Image-to-ASCII Converter (with Colour Support)

This project converts an image into an ASCII art representation using Python, where the ASCII characters are matched with the colour values from the original image. The output is displayed directly within a Jupyter notebook.

## Features

- **Full Colour Support**: Unlike traditional black-and-white ASCII art, this version reflects the colour values of the original image.
- **Customisable Output**: Adjust the number of horizontal and vertical ASCII characters for different output sizes.
- **Preserved Grayscale**: Carefully selected characters based on brightness to provide a more visually accurate representation.
- **Easy Integration with Jupyter Notebooks**: View the resulting coloured ASCII art directly within your notebook environment.

## Requirements

- Python 3.x
- Libraries: `Pillow`, `IPython`
- Jupyter Notebook environment

To install the required libraries, run:

```bash
pip install pillow ipython
```

## Usage

### 1. **Display Image**
To display the image inside a Jupyter Notebook cell:

```python
from IPython.display import display
from PIL import Image

def show_image(image_path):
    image = Image.open(image_path)
    display(image)

# Usage example:
# show_image("path_to_image.jpg")
```

### 2. **Convert Image to ASCII**
To convert the image into ASCII art, preserving the colours, run the following code:

```python
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
```

### Parameters:
- `image_path`: Path to the image file you want to convert.
- `new_width` (optional): Number of horizontal characters in the output. Default is 100.
- `new_height` (optional): Number of vertical characters in the output. Default is 50.

### Example:
If you want to convert an image at `"image.jpg"` to ASCII with a width of 100 characters and a height of 50:

```python
display_ascii("image.jpg", 100, 50)
```

This will generate the ASCII art in the notebook, preserving the colours of the original image.

## License

This project is open-source and available under the MIT License. Feel free to use and modify the code for your personal or educational purposes.

---

This README provides an overview of how to set up and use the Image-to-ASCII converter with colour support in a Jupyter Notebook. Enjoy creating colourful ASCII art!