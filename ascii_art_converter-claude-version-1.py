""" Prompt for this version: Write a python program which takes a png image as an input and converts it into an ASCII which visually looks fairly similar to the original input image, without using numpy
"""

from PIL import Image


def get_ascii_char(pixel_value):
    # ASCII characters from darkest to lightest
    ascii_chars = '@%#*+=-:. '
    # Map the 0-255 pixel value to the ascii_chars list index
    index = int((pixel_value / 255) * (len(ascii_chars) - 1))
    return ascii_chars[index]


def image_to_ascii(image_path, output_width=100):
    # Open and convert image to grayscale
    try:
        img = Image.open(image_path).convert('L')
    except Exception as e:
        return f"Error opening image: {str(e)}"

    # Calculate new dimensions while maintaining aspect ratio
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * output_width * 0.5)  # * 0.5 to account for terminal line spacing

    # Resize image
    img = img.resize((output_width, new_height))

    # Convert pixels to ASCII
    ascii_image = []
    pixels = list(img.getdata())

    # Process all pixels and convert to ASCII characters
    for i in range(0, len(pixels), output_width):
        row = pixels[i:i + output_width]
        ascii_row = ''.join(get_ascii_char(pixel) for pixel in row)
        ascii_image.append(ascii_row)

    return '\n'.join(ascii_image)


def save_ascii_art(ascii_art, output_path):
    try:
        with open(output_path, 'w') as f:
            f.write(ascii_art)
        return True
    except Exception as e:
        print(f"Error saving ASCII art: {str(e)}")
        return False


def main():
    # Example usage
    input_path = input("Enter the path to your PNG image: ")
    output_width = input("Enter desired output width (default 100): ")

    # Set default width if empty input
    output_width = int(output_width) if output_width.strip() else 100

    # Convert image to ASCII
    ascii_art = image_to_ascii(input_path, output_width)

    # Print to console
    print("\nASCII Art:")
    print(ascii_art)

    # Save to file
    save_choice = input("\nWould you like to save the ASCII art to a file? (y/n): ")
    if save_choice.lower() == 'y':
        output_path = input("Enter output file path: ")
        if save_ascii_art(ascii_art, output_path):
            print(f"ASCII art saved to {output_path}")
        else:
            print("Failed to save ASCII art")


if __name__ == "__main__":
    main()