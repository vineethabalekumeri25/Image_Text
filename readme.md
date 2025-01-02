# README

## Overview
This project combines OCR (Optical Character Recognition) and OpenAI API to:
1. Extract text from an image using Tesseract OCR.
2. Highlight specific text in the image.
3. Send the extracted text to the OpenAI API for further analysis or processing.

## Prerequisites
Before running this project, ensure you have the following installed and configured:

### Dependencies
- Python 3.7+
- Required Python libraries:
  - `openai`
  - `Pillow`
  - `pytesseract`
  - `python-dotenv`

### Additional Requirements
- **Tesseract OCR**:
  - Install Tesseract OCR on your system.
  - Update the path to the Tesseract executable in the script:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    ```
    Replace the path with the correct location for your system.

- **OpenAI API Key**:
  - Obtain an API key from the [OpenAI platform](https://platform.openai.com/account/api-keys).
  - Save the API key in a `.env` file in the following format:
    ```
    OPENAI_API_KEY=your-api-key-here
    ```

## Setup
1. **Install Python Dependencies**:
   ```bash
   pip install openai Pillow pytesseract python-dotenv
   ```

2. **Create and Configure `.env` File**:
   - In the project directory, create a file named `.env`.
   - Add the following line:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

3. **Prepare Tesseract**:
   - Download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract).
   - Update the `pytesseract.pytesseract.tesseract_cmd` path in the script to match your system.

4. **Add an Image**:
   - Place the image you want to process in the project directory.
   - Update the `image_file` variable in the script to point to your image file.

## Running the Script
1. Run the script:
   ```bash
   python script_name.py
   ```

2. **Functionality**:
   - The script will:
     1. Extract text from the specified image.
     2. Send the extracted text to OpenAI for analysis.
     3. Highlight user-specified text in the image.

3. **Input and Output**:
   - Enter the text you want to highlight when prompted.
   - The output image with highlighted text will be saved to `highlighted_image.jpg` (default name).

## Functions

### `extract_text_from_image(image_path)`
- Extracts text from an image using Tesseract OCR.
- **Parameters**:
  - `image_path`: Path to the image file.
- **Returns**: Extracted text as a string.

### `highlight_text_in_image(image_path, text_to_highlight, output_path)`
- Highlights specified text in the image.
- **Parameters**:
  - `image_path`: Path to the image file.
  - `text_to_highlight`: Text to search for and highlight.
  - `output_path`: Path to save the highlighted image.

### `send_text_to_openai(text)`
- Sends text to OpenAI for analysis.
- **Parameters**:
  - `text`: The text to analyze.
- **Returns**: OpenAI API response as a string.

## Example Workflow
1. The script extracts text from `image.jpg`.
2. The extracted text is sent to OpenAI for analysis.
3. The user specifies text to highlight in the image.
4. The highlighted image is saved as `highlighted_image.jpg`.

## Notes
- Ensure the `.env` file is secure and not shared publicly.
- Use environment variables to manage sensitive data like API keys.
- Modify the script to suit your specific use case as needed.

## Troubleshooting
- **Invalid API Key Error**:
  - Ensure the API key in `.env` is correct.
  - Regenerate the API key if necessary.
- **Tesseract Not Found**:
  - Verify the `tesseract_cmd` path matches your system installation.
- **Text Not Highlighted**:
  - Ensure the text to highlight matches the OCR output (case-insensitive).

## License
This project is for educational purposes. Modify and distribute as needed for personal or commercial use.

