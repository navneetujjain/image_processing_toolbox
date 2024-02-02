import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
from compression_column import column_compress_image
from compression_row import row_compress_image
from hpf import highpass_image
from lpf import lowpass_image
from compression_total import process_image
from ttkthemes import ThemedTk

def high_pass_filter(image_path):
    highpass_image(image_path)
    return image_path
    
def low_pass_filter(image_path):
    lowpass_image(image_path)
    return image_path
    
def row_compression(image_path):
    row_compress_image(image_path)
    return image_path
    
def column_compression(image_path):
    column_compress_image(image_path)
    return image_path

def total_compression(image_path):
    process_image(image_path)
    return image_path

class ImageProcessorApp:
    def __init__(self, root):
        self.root = ThemedTk(theme="radiance")
        self.root.title("Image Processing Toolbox")

        # Variables
        self.image_path = tk.StringVar()

        # GUI Components
        ttk.Label(self.root, text="Enter Image Path:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        ttk.Entry(self.root, textvariable=self.image_path, width=40).grid(row=0, column=1, padx=10, pady=10, sticky="we")
        ttk.Button(self.root, text="Browse", command=self.browse_image).grid(row=0, column=2, padx=10, pady=10)

        # Buttons
        buttons = ["High Pass Filter", "Low Pass Filter", "Column Compression", "Row Compression", "Total Compression"]
        functions = [high_pass_filter, low_pass_filter, row_compression, column_compression, total_compression]

        for i, button_text in enumerate(buttons):
            ttk.Button(self.root, text=button_text, command=lambda func=functions[i]: self.process_image(func)).grid(row=i + 1, column=0, columnspan=3, padx=10, pady=5, sticky="we")

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image_path.set(file_path)

    def process_image(self, function):
        image_path = self.image_path.get()
        if image_path:
            try:
                result_image = function(image_path)
                messagebox.showinfo("Success", "Image processing action successfully performed!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showwarning("Warning", "Please select an image first.")

if __name__ == "__main__":
    app = ImageProcessorApp(None)
    app.root.mainloop()
