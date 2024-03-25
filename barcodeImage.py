import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
import random
import string

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")

        # Create a frame for serial number input and generation
        self.serial_frame = tk.Frame(root)
        self.serial_frame.pack()

        # Serial number input
        self.serial_number_label = tk.Label(self.serial_frame, text="Enter Serial Number:")
        self.serial_number_label.pack(side=tk.LEFT)

        self.serial_number_entry = tk.Entry(self.serial_frame)
        self.serial_number_entry.pack(side=tk.LEFT)

        # Button to generate serial number
        self.generate_serial_button = tk.Button(self.serial_frame, text="Generate Serial Number", command=self.generate_different_serial)
        self.generate_serial_button.pack(side=tk.LEFT)

        # Create a frame for QR code display
        self.qr_frame = tk.Frame(root)
        self.qr_frame.pack()

        # Label to display generated serial number
        self.generated_serial_label = tk.Label(self.qr_frame, text="Generated Serial Number:")
        self.generated_serial_label.pack()

        self.generated_serial_entry = tk.Entry(self.qr_frame)
        self.generated_serial_entry.pack()

        # Create a label to display the QR code image
        self.qr_label = tk.Label(self.qr_frame)
        self.qr_label.pack()

    def generate_qr_code(self, serial_number):
        if serial_number:
            try:
                # Create QR code instance
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )

                # Add data to the QR code
                qr.add_data(serial_number)
                qr.make(fit=True)

                # Create an image from the QR code instance
                img = qr.make_image(fill_color="black", back_color="white")

                # Convert PIL Image to Tkinter PhotoImage
                qr_image = ImageTk.PhotoImage(img)

                # Display the QR code image on the label
                self.qr_label.config(image=qr_image)
                self.qr_label.image = qr_image  # Keep a reference to prevent garbage collection
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showerror("Error", "Please enter a serial number.")

    def generate_different_serial(self):
        original_serial = self.serial_number_entry.get()
        if original_serial:
            try:
                # Generate a different serial number
                random_part_length = len(original_serial) - 2  # Excluding the '0x' prefix
                random_part = ''.join(random.choices(string.hexdigits, k=random_part_length))
                different_serial = original_serial[:2] + random_part
                # Display the generated serial number
                self.generated_serial_entry.delete(0, tk.END)
                self.generated_serial_entry.insert(0, different_serial)
                # Generate the QR code for the new serial number
                self.generate_qr_code(different_serial)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showerror("Error", "Please enter an original serial number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
