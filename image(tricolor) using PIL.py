NumPy Image Creation Using NumPy, create an image of at least 100 x 100 pixels!


import numpy as np
from PIL import Image

# Create a blank image with white background
width, height = 100, 100
image_data = np.ones((height, width, 3), dtype=np.uint8) * 255

# Create a red square in the center
center_x, center_y = width // 2, height // 2
square_size = 30
image_data[center_y - square_size // 2:center_y + square_size // 2,
           center_x - square_size // 2:center_x + square_size // 2] = [255, 0, 0]

# Create a PIL image from NumPy array
image = Image.fromarray(image_data)

# Save the image
image.save("numpy_image.png")
print("Image saved as 'numpy_image.png'")
