# Image to PDF Converter

## Description

This project allows you to convert scanned pages of a book into a single PDF file. The scanned images undergo preprocessing, including cropping and splitting, to ensure that each page is correctly formatted in the final PDF.

## Features

- Configurable cropping settings via an environment file.
- Splits double pages into two separate pages.
- Processes images in test mode to verify configurations.
- Outputs a single PDF file containing all processed pages.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd pdfCreator
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file based on the `example.env` file and configure the cropping settings.

## Usage

To run the program, execute the following command:

```bash
python image_to_pdf.py
```

## Configuration

The cropping settings and other parameters can be configured in the `.env` file. The parameters include:

- `CROP_LEFT`: Amount to crop from the left side (in pixels).
- `CROP_RIGHT`: Amount to crop from the right side (in pixels).
- `CROP_TOP`: Amount to crop from the top (in pixels).
- `CROP_BOTTOM`: Amount to crop from the bottom (in pixels).
- `TEST_MODE`: Set to `True` to enable test mode.
- `TEST_OFFSET`: Offset for selecting images in test mode.
- `TEST_SAMPLE_SIZE`: Number of images to process in test mode.
- `TARGET_WIDTH`: Target width for resizing images (in pixels).
- `TARGET_HEIGHT`: Target height for resizing images (in pixels).

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
