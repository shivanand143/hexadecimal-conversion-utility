import tkinter as tk
from tkinter import messagebox
import base64

# Function to convert hex to ASCII (using latin-1 to avoid errors)
def hex_to_ascii(hex_str):
    try:
        return bytes.fromhex(hex_str).decode('utf-8')  # Try decoding to UTF-8
    except UnicodeDecodeError:
        return bytes.fromhex(hex_str).decode('latin-1')  # Fallback to latin-1 decoding

# Function to convert hex to Unknown (Base64 encoding)
def hex_to_unknown(hex_str):
    ascii_str = hex_to_ascii(hex_str)
    return base64.b64encode(ascii_str.encode('utf-8')).decode('utf-8')

# Function to convert Base64 to Hex
def base64_to_hex(base64_str):
    decoded_bytes = base64.b64decode(base64_str)
    return decoded_bytes.hex()

# Function to process and display conversions
def process_hex():
    hex_str = hex_entry.get()  # Get the hex string entered by the user
    if hex_str:  # Check if the hex string is not empty
        # Convert Hex to ASCII
        converted_ascii = hex_to_ascii(hex_str)
        ascii_value_text.delete(1.0, tk.END)
        ascii_value_text.insert(tk.END, converted_ascii)

        # Convert Hex to Unknown (Base64 encoded)
        converted_unknown = hex_to_unknown(hex_str)
        unknown_value_text.delete(1.0, tk.END)
        unknown_value_text.insert(tk.END, converted_unknown)

        # Convert Base64 back to Hex
        decoded_hex = base64_to_hex(converted_unknown)
        decoded_hex_value_text.delete(1.0, tk.END)
        decoded_hex_value_text.insert(tk.END, decoded_hex)

        # Clear the entry field for new data input
        hex_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a valid hex string.")

# Function to reset the UI for a new input
def reset_ui():
    # Clear the conversion result text areas
    ascii_value_text.delete(1.0, tk.END)
    unknown_value_text.delete(1.0, tk.END)
    decoded_hex_value_text.delete(1.0, tk.END)

# Set up the main window using Tkinter
root = tk.Tk()
root.title("Hex Converter Tool")

# Project Headline
headline_label = tk.Label(root, text="Hex to ASCII, Unknown (Base64), and Back Converter", font=("Arial", 16, "bold"))
headline_label.pack(pady=10)

# Hex Input Section
hex_label = tk.Label(root, text="Enter Hex String:", font=("Arial", 12))
hex_label.pack(pady=5)

hex_entry = tk.Entry(root, width=60, font=("Arial", 12))
hex_entry.pack(pady=10)

# Process Button
process_button = tk.Button(root, text="Process Hex", font=("Arial", 12), command=process_hex)
process_button.pack(pady=10)

# Converted Text Output
output_frame = tk.Frame(root)
output_frame.pack(pady=10)

# Structured Output Labels
output_title_label = tk.Label(output_frame, text="Conversion Results", font=("Arial", 14, "bold"))
output_title_label.pack(pady=5)

ascii_label = tk.Label(output_frame, text="Hex to ASCII:", font=("Arial", 12))
ascii_label.pack(pady=5)

# Text widget to show Hex to ASCII output
ascii_value_text = tk.Text(output_frame, font=("Arial", 12), height=6, width=80, wrap=tk.WORD)
ascii_value_text.pack(pady=5)

unknown_label = tk.Label(output_frame, text="Hex to Unknown (Base64):", font=("Arial", 12))
unknown_label.pack(pady=5)

# Text widget to show Hex to Unknown (Base64) output
unknown_value_text = tk.Text(output_frame, font=("Arial", 12), height=6, width=80, wrap=tk.WORD)
unknown_value_text.pack(pady=5)

decoded_hex_label = tk.Label(output_frame, text="Base64 to Hex (decoded):", font=("Arial", 12))
decoded_hex_label.pack(pady=5)

# Text widget to show Base64 to Hex output
decoded_hex_value_text = tk.Text(output_frame, font=("Arial", 12), height=6, width=80, wrap=tk.WORD)
decoded_hex_value_text.pack(pady=5)

# Check Another Button
check_another_button = tk.Button(root, text="Check Another", font=("Arial", 12), command=reset_ui)
check_another_button.pack(pady=20)

# Start the GUI loop
root.mainloop()
