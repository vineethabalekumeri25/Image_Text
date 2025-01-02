import openai
from PIL import Image, ImageDraw
import pytesseract
import os
from dotenv import load_dotenv

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update this path for your system

# Load environment variables from the .env file
load_dotenv()
# Retrieve the API key
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("API key not found. Please set it in the .env file.")

openai.api_key = openai_api_key

try:
    response = openai.Model.list()
    print("API Key is valid. Available models:", response)
except openai.error.AuthenticationError:
    print("Invalid API Key!")

def extract_text_from_image(image_path):
    """
    Extract text from an image using pytesseract.

    :param image_path: Path to the image file.
    :return: Extracted text as a string.
    """
    try:
        # Open the image using PIL (Python Imaging Library)
        image = Image.open(image_path)

        # Perform OCR using pytesseract
        text = pytesseract.image_to_string(image)

        return text
    except Exception as e:
        return f"Error: {e}"

def highlight_text_in_image(image_path, text_to_highlight, output_path):
    """
    Highlight specific text in an image.

    :param image_path: Path to the image file.
    :param text_to_highlight: The text to search for and highlight.
    :param output_path: Path to save the highlighted image.
    """
    try:
        # Open the image
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        # Perform OCR using pytesseract to get bounding box data
        data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

        # Loop through the detected text
        for i in range(len(data['text'])):
            detected_text = data['text'][i].strip()
            if text_to_highlight.lower() in detected_text.lower():  # Case-insensitive search
                x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
                draw.rectangle([x, y, x + w, y + h], outline="blue", width=2)

        # Save the highlighted image
        image.save(output_path)
        print(f"Highlighted image saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def send_text_to_openai(text):
    """
    Send the extracted text to OpenAI API for processing.

    :param text: The extracted text to send to OpenAI.
    :return: Response from OpenAI API.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Analyze the following text:\n{text}"}
            ],
            max_tokens=200
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    image_file = "image.jpg"  # Replace with your image file path
    extracted_text = extract_text_from_image(image_file)
    print("Extracted Text:")
    print(extracted_text)

    # Send extracted text to OpenAI API
    openai_response = send_text_to_openai(extracted_text)
    print("\nOpenAI API Response:")
    print(openai_response)

    output_file = "highlighted_image.jpg"  # Output file path

    # Get text input from the user
    text_to_find = input("\nEnter the text to highlight: ")

    highlight_text_in_image(image_file, text_to_find, output_file)
