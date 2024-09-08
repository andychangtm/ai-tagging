import os
from PIL import Image

IMAGE_FOLDER = "input"

def compress_image(image_path):
    image = Image.open(image_path)
    width, height = image.size
    new_size = (width // 2, height // 2)
    resized_image = image.resize(new_size)
    resized_image.save(image_path, optimize=True, quality=20)

if __name__ == "__main__":
    for filename in os.listdir(IMAGE_FOLDER):
            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                image_path = os.path.join(IMAGE_FOLDER, filename)
                compress_image(image_path)
    print("Compression of images completed!")
