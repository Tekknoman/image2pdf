import os
from dotenv import load_dotenv
from PIL import Image
import img2pdf
from tqdm import tqdm  # Import tqdm for progress bars
from config_manager import Config


def process_images(input_dir, config):
    images = [f for f in os.listdir(input_dir) if f.endswith((".png", ".jpg", ".jpeg"))]
    processed_image_paths = []

    for image_name in tqdm(images, desc="Processing images"):
        image_path = os.path.join(input_dir, image_name)
        with Image.open(image_path) as img:
            img_resized = img.resize(
                (config.TARGET_WIDTH, config.TARGET_HEIGHT), Image.Resampling.LANCZOS
            )
            img_cropped = img_resized.crop(
                (
                    config.CROP_LEFT,
                    config.CROP_TOP,
                    img_resized.width - config.CROP_RIGHT,
                    img_resized.height - config.CROP_BOTTOM,
                )
            )
            width, height = img_cropped.size
            left_page = img_cropped.crop((0, 0, width // 2, height))
            right_page = img_cropped.crop((width // 2, 0, width, height))
            left_page_path = os.path.join(
                config.processed_images_dir, f"left_{image_name}"
            )
            right_page_path = os.path.join(
                config.processed_images_dir, f"right_{image_name}"
            )
            left_page.save(left_page_path)
            right_page.save(right_page_path)
            processed_image_paths.append(left_page_path)
            processed_image_paths.append(right_page_path)

    with open(config.output_pdf, "wb") as f:
        f.write(img2pdf.convert(processed_image_paths))


if __name__ == "__main__":
    load_dotenv(".env")
    config = Config()
    input_dir = "input/"  # Default input directory
    process_images(input_dir, config)
