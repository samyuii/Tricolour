# Task 7: NumPy Image Creation Using NumPy, create an image of at least 100 x 100 pixels!


from PIL import Image, ImageDraw


def draw_indian_flag():
    height = 225
    width = 450

    # Create a new image with white background
    flag = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(flag)

    # Calculate the heights of different sections in the flag
    saffron_height = height // 3
    white_height = height // 3
    green_height = height // 3

    # Draw the saffron, white, and green sections
    draw.rectangle([(0, 0), (width, saffron_height)], fill=(255, 153, 51))
    draw.rectangle([(0, saffron_height), (width, saffron_height + white_height)], fill=(255, 255, 255))
    draw.rectangle([(0, saffron_height + white_height), (width, height)], fill=(19, 136, 8))

    flag.save("indian_flag.png")
    flag.show()


if __name__ == "__main__":
    draw_indian_flag()