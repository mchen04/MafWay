from PIL import Image, ImageDraw
import os

# Create directory if it doesn't exist
upload_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'user_inputs')
os.makedirs(upload_dir, exist_ok=True)

# Create a new image with a white background
image = Image.new('L', (45, 45), 'white')
draw = ImageDraw.Draw(image)

# Draw an exclamation mark
draw.text((20, 20), '!', fill='black')

# Save the image
image_path = os.path.join(upload_dir, 'test.jpg')
image.save(image_path)
print(f"Created test image at: {image_path}")

# Verify file exists
if os.path.exists(image_path):
    print("File exists and is accessible")
    print(f"File size: {os.path.getsize(image_path)} bytes")
