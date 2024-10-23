import os
from dotenv import load_dotenv
from PIL import Image
import img2pdf
from tqdm import tqdm  # Import tqdm for progress bars

# Load environment variables
load_dotenv("example.env")

# Configuration
CROP_LEFT = int(os.getenv("CROP_LEFT", 0))
CROP_RIGHT = int(os.getenv("CROP_RIGHT", 0))
CROP_TOP = int(os.getenv("CROP_TOP", 0))
CROP_BOTTOM = int(os.getenv("CROP_BOTTOM", 0))
TEST_MODE = os.getenv("TEST_MODE", "False").lower() == "true"
TEST_SAMPLE_SIZE = int(os.getenv("TEST_SAMPLE_SIZE", 5))
TEST_OFFSET = int(os.getenv("TEST_OFFSET", 0))
TARGET_WIDTH = int(os.getenv("TARGET_WIDTH", 800))
TARGET_HEIGHT = int(os.getenv("TARGET_HEIGHT", 600))

# Input and output directories
input_dir = "input/"
output_pdf = "output.pdf"
processed_images_dir = "processed_images/"

# Create the processed images directory if it doesn't exist
os.makedirs(processed_images_dir, exist_ok=True)


def process_images():
    images = [f for f in os.listdir(input_dir) if f.endswith((".png", ".jpg", ".jpeg"))]

    if TEST_MODE:
        images = images[TEST_OFFSET : TEST_OFFSET + TEST_SAMPLE_SIZE]

    processed_image_paths = []

    # Wrap the loop with tqdm for progress indication
    for image_name in tqdm(images, desc="Processing images"):
        image_path = os.path.join(input_dir, image_name)
        with Image.open(image_path) as img:
            # Resize the image to the target dimensions
            img_resized = img.resize(
                (TARGET_WIDTH, TARGET_HEIGHT), Image.Resampling.LANCZOS
            )

            # Crop the image
            img_cropped = img_resized.crop(
                (
                    CROP_LEFT,
                    CROP_TOP,
                    img_resized.width - CROP_RIGHT,
                    img_resized.height - CROP_BOTTOM,
                )
            )

            # Split the image into two pages
            width, height = img_cropped.size
            left_page = img_cropped.crop((0, 0, width // 2, height))
            right_page = img_cropped.crop((width // 2, 0, width, height))

            # Save the processed images in the new directory
            left_page_path = os.path.join(processed_images_dir, f"left_{image_name}")
            right_page_path = os.path.join(processed_images_dir, f"right_{image_name}")
            left_page.save(left_page_path)
            right_page.save(right_page_path)

            processed_image_paths.append(left_page_path)
            processed_image_paths.append(right_page_path)

    # Create a PDF from the processed images
    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(processed_image_paths))


if __name__ == "__main__":
    process_images()
