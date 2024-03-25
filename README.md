# Generate-QR-Code-with-image

```markdown
# QR Code Generator App

This application allows users to generate QR codes based on serial numbers provided. It provides functionality to input a serial number manually or generate a random serial number, display the serial number, and generate a corresponding QR code.

## Usage

To use the QR Code Generator App:

1. Run the script.
2. Enter a serial number in the input field.
3. Click on the "Generate Serial Number" button to generate a different serial number based on the original one provided.
4. The generated serial number will be displayed in the entry field labeled "Generated Serial Number."
5. The corresponding QR code for the generated serial number will be displayed.

## Dependencies

- Python 3.x
- tkinter
- qrcode
- Pillow (PIL)

## Installation

You can install the required dependencies using pip:

```
pip install qrcode pillow
```

## How It Works

1. Upon launching the application, a tkinter window opens with an entry field to input the original serial number and a button to generate a different serial number.

2. The `generate_different_serial` method is triggered when the "Generate Serial Number" button is clicked. It generates a different serial number based on the original one provided, by replacing part of the original serial number with random hexadecimal characters. The generated serial number is displayed in the corresponding entry field.

3. The `generate_qr_code` method generates a QR code image based on the provided serial number. It utilizes the `qrcode` library to create the QR code instance, adds data to it, and then converts the generated QR code image from a PIL Image to a Tkinter PhotoImage. The QR code image is then displayed on a tkinter label.

4. Error handling is implemented to handle exceptions that may occur during the generation process, and error messages are displayed using tkinter messagebox.

## Author

This QR Code Generator App was created by Ahmed Alzeidi.
```
