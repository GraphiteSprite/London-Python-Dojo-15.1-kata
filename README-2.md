/// Please update the README to reflect the recent changes


# Image to ASCII Art Converter

A Python program that converts various image formats into ASCII art, creating text-based representations that preserve the visual essence of the original image. This tool transforms images into ASCII characters, with different characters representing different levels of brightness.

## Features

- Supports multiple image formats:
  - JPEG (.jpg, .jpeg)
  - PNG (.png)
  - BMP (.bmp)
  - GIF (.gif) - including first frame of animated GIFs
  - WebP (.webp)
  - TIFF (.tiff)
- Maintains aspect ratio during conversion
- Customizable output width
- Supports both console display and file saving
- Simple command-line interface
- No numpy dependency required
- Comprehensive error handling
- Special handling for animated GIFs

## Prerequisites

- Python 3.x
- PIL (Python Imaging Library)

Install the required dependency using pip:
```bash
pip install Pillow
```

## Installation

1. Clone or download the script to your local machine
2. Ensure you have the prerequisites installed
3. Run the script using Python 3

## Usage

1. Run the script:
```bash
python ascii_art_converter.py
```

2. Follow the prompts:
   - View supported image formats
   - Enter the path to your image
   - Specify desired output width (default is 100 characters)
   - Choose whether to save the output to a file

## How It Works

The converter uses the following process:

1. Image Processing:
   - Validates the input file format
   - Loads the image using PIL
   - Handles special cases (e.g., animated GIFs)
   - Converts it to grayscale
   - Resizes while maintaining aspect ratio

2. ASCII Conversion:
   - Maps pixel brightness values (0-255) to ASCII characters
   - Uses a character set from darkest to lightest: @%#*+=-:. 
   - Generates ASCII art line by line

3. Output:
   - Displays the result in the console
   - Optionally saves to a text file

## Example Usage

```python
# Using as a module
from ascii_art_converter import image_to_ascii, get_supported_formats

# Check supported formats
print(get_supported_formats())

# Convert an image
ascii_art = image_to_ascii("path/to/your/image.jpg", output_width=100)
print(ascii_art)
```

## Special Cases

### Animated GIFs
- For animated GIFs, the converter processes only the first frame
- A notification is displayed when processing animated GIFs
- The resulting ASCII art represents the first frame of the animation

## Error Handling

The program includes error handling for:
- Unsupported file formats
- Non-existent files
- Invalid image files
- File saving problems
- Animated GIF processing

## Limitations

- Works best with images that have good contrast
- Output quality depends on terminal/font settings
- Very small details might be lost in conversion
- Terminal line spacing affects the final appearance
- Only the first frame is used for animated GIFs

## Customization

You can modify the ASCII character set in the `get_ascii_char` function to use different characters for the brightness levels. The current set (`@%#*+=-:. `) goes from darkest to lightest.

## Contributing

Feel free to fork this project and submit improvements through pull requests. Some areas for potential enhancement:
- Additional image format support
- Color ASCII art
- More character sets
- GUI interface
- Full animated GIF support
- Custom ASCII character sets

## License

This project is available under the MIT License. Feel free to use, modify, and distribute as needed.