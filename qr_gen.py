import tkinter as tk
from tkinter import ttk
import qrcode
import subprocess

def generate_qr():
    with open("script.sh", "r") as file:
        script_content = file.read()
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(script_content)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    subprocess.run(["xdg-open", "qrcode.png"])


root = tk.Tk()
root.title("QR Code Generator")

style = ttk.Style()
style.theme_use('clam')  # Choose your desired theme

# Create and place widgets
label = ttk.Label(root, text="Enter text:")
label.grid(row=0, column=0, padx=10, pady=10)

input_box = ttk.Entry(root, width=50)
input_box.grid(row=0, column=1, padx=10, pady=10)

generate_button = ttk.Button(root, text="Generate QR", command=generate_qr)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
