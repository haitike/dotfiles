import os
import pytesseract
import argparse
from PIL import Image, ImageDraw, ImageFilter, ImageOps

from utilidades import imprimir_warning

# Define the text to search for in images
DIRECTORIES = ["cylex", "hotfrog", "firmania", "locanto"]
WP_ADMIN_STRINGS = ["wp-login", "upload", "page=nestedpages", "action=edit", "action=elementor"]

# Utility Functions
def preprocess_image(image):
    """Preprocess image for OCR."""
    gray = ImageOps.grayscale(image)
    contrast = ImageOps.autocontrast(gray)
    blurred = contrast.filter(ImageFilter.GaussianBlur(1))
    return blurred


def calculate_text_rectangle(text, initial_x=144, padding=20):
    """Calculate rectangle width based on text length."""
    text_width = len(text) * 7.5  # Approximate width of each character
    rectangle_width = initial_x + text_width + padding
    return rectangle_width


def draw_rectangles(draw, rectangles, outline="red", width=4):
    """Draw rectangles on the image."""
    for rect in rectangles:
        draw.rectangle(rect, outline=outline, width=width)

# Don Dominio
def process_dominio(draw, filename):
    print(filename)
    """Specific processing for Don Dominio pages."""
    if "titu" in filename:
        draw_rectangles(draw, [(390, 300, 1090, 795), (390, 900, 740, 1025)])
        return f"marked_{filename}"
    elif "ip" in filename:
        draw_rectangles(draw, [(570, 195, 1300, 490), (570, 520, 1300, 810)])
        return f"marked_{filename}"
    elif "fecha" in filename:
        draw_rectangles(draw, [(385, 240, 960, 350), (385, 355, 1330, 460), (385, 480, 850, 725), (385, 740, 850, 890)])
        return f"marked_{filename}"
    elif "whois" in filename:
        draw_rectangles(draw, [(350, 240, 900, 315), (380, 460, 880, 1375)])
        return f"marked_{filename}"
    return filename

# Directorios de empresas -specific rectangle drawing
def process_directories(draw, detected_directory, filename, address_text, has_open_hours):
    """Process and draw rectangles for directory-specific logic."""
    directory_rectangles = {
        "cylex": [(380, 113, 600, 170), (380, 195, 1250, 515)],
        "hotfrog": [(390, 415, 1120, 715), (1230, 295, 1515, 400)],
        "firmania": [(190, 90, 400, 180), (190, 350, 1050, 755)],
        "locanto": [(270, 90, 440, 150), (450, 105, 500 + calculate_text_rectangle(address_text.split('/')[-1]), 145)]
    }

    if has_open_hours:
        directory_rectangles = {
            "cylex": [(380, 113, 600, 170)],
            "hotfrog": [(1230, 295, 1515, 400)],
            "firmania": [(190, 90, 400, 180)],
            "locanto": [(270, 90, 440, 150),
                        (450, 105, 500 + calculate_text_rectangle(address_text.split('/')[-1]), 145)]
        }

    draw_rectangles(draw, directory_rectangles.get(detected_directory, []))
    if detected_directory == "hotfrog":
        draw.rectangle((390, 90, 570, 140), outline="yellow", width=4)

    return f"{detected_directory}_{filename}"


# WP-Admin specific rectangle drawing
def process_wp_admin(draw, detected_wp_admin, filename):
    """Process and draw rectangles for wp-admin specific logic."""
    wp_admin_rectangles = {
        "wp-login": [(800, 290, 1120, 700)],
        "upload": [(2, 210, 160, 360), (180, 260, 1900, 925)],
        "page=nestedpages": [(2, 240, 160, 400), (200, 275, 920, 325)],
        "action=edit": [(700, 430, 930, 475)],
        "action=elementor": [(2, 130, 300, 940)],
    }

    draw_rectangles(draw, wp_admin_rectangles.get(detected_wp_admin, []))
    return f"{detected_wp_admin}_{filename}"


def process_translate_pages(draw, address_text, filename):
    """Specific processing for translate pages."""
    if "translate" in address_text:
        draw_rectangles(draw, [(260, 180, 390, 215), (400, 330, 950, 465), (400, 530, 660, 710), (2, 690, 160, 1000)])
        return f"translate-settings_{filename}"
    elif "plugins" in address_text:
        draw_rectangles(draw, [(180, 395, 1880, 465), (2, 540, 160, 575)])
        return f"translate-plugin_{filename}"
    return filename


def process_devices(draw, device_text, filename):
    """Detect device type from OCR text."""
    if "Escritorio" in device_text:
        draw.rectangle((735, 85, 1175, 115), outline="red", width=4)
        return f"escritorio_{filename}"
    elif "Samsung Galaxy" in device_text:
        draw.rectangle((630, 85, 1175, 115), outline="red", width=4)
        return f"movil_{filename}"
    elif "Pad" in device_text:
        draw.rectangle((735, 85, 1175, 115), outline="red", width=4)
        return f"tablet_{filename}"
    return filename


def process_image(filename, img, current_dir_name, address_text, has_open_hours):
    draw = ImageDraw.Draw(img)
    new_filename = filename

    if current_dir_name == '5':
        detected_directory = next((directory for directory in DIRECTORIES if directory in address_text.lower()), None)
        if detected_directory:
            new_filename = process_directories(draw, detected_directory, filename, address_text, has_open_hours)
    elif current_dir_name == '4':
        print(address_text)
        detected_wp_admin = next((string for string in WP_ADMIN_STRINGS if string in address_text), None)
        if detected_wp_admin:
            new_filename = process_wp_admin(draw, detected_wp_admin, filename)
    elif current_dir_name == '3':
        device_text = pytesseract.image_to_string(preprocess_image(img.crop((0, 85, 1800, 115))), config='--psm 6')
        new_filename = process_devices(draw, device_text, filename)
    elif current_dir_name == '6.1':
        new_filename = process_translate_pages(draw, address_text, filename)
    elif current_dir_name == '1':
        new_filename = process_dominio(draw, filename)
    else:
        new_filename = f"marked_{filename}"

    # Always draw the Address Bar Rectangle
    rectangle_width = calculate_text_rectangle(address_text)
    draw.rectangle((144, 45, rectangle_width + 40, 80), outline="red", width=4)

    return new_filename


def main(input_folder, output_folder):

    #Set up argument parser
    parser = argparse.ArgumentParser(description="Process images with OCR and draw rectangles based on detected text.")
    parser.add_argument("-o", "--has_open_hours", action="store_true",
                        help="Specify if the images contain open hours information.")
    args = parser.parse_args()

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)


    # Walk through the input folder recursively
    for root, _, files in os.walk(input_folder):
        if not files:
            continue  # Skip empty directories

        current_dir_name = os.path.basename(root)
        output_subfolder = os.path.join(output_folder, os.path.relpath(root, input_folder))
        os.makedirs(output_subfolder, exist_ok=True)

        for filename in files:
            if not filename.lower().endswith((".jpg", ".png")):
                continue  # Skip non-image files

            file_path = os.path.join(root, filename)

            with Image.open(file_path) as img:
                # Get the Address Bar text
                address_bar_roi = img.crop((144, 45, 1280, 80))
                processed_roi = preprocess_image(address_bar_roi)
                address_text = pytesseract.image_to_string(processed_roi, config='--psm 6')

                # Process image and get the new filename if renamed
                new_filename = process_image(filename, img, current_dir_name, address_text, args.has_open_hours)

                # Save the processed image to the output folder
                output_path = os.path.join(output_subfolder, new_filename)
                img.save(output_path)
                print(f"Processed and saved: {output_path}")

if __name__ == '__main__':
    main("images", "images_justificated" )
