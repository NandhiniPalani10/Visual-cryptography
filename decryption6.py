# This code uses two share images to combine them using XOR operation, and then save the decrypted image. 
# The ^ operator in Python performs the XOR operation between two bits. 
# The code also checks that the share images have the same size before combining them.

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageOps
import random



# Function to handle button click
def decrypt_image():
    # Get the filenames of the share images using a file dialog
    share1_filename = filedialog.askopenfilename(title="Select Share 1", filetypes=[("PNG files", "*.png")])
    share2_filename = filedialog.askopenfilename(title="Select Share 2", filetypes=[("PNG files", "*.png")])

    # Load the share images
    share1 = Image.open(share1_filename)
    share2 = Image.open(share2_filename)

    # Verify that the share images have the same size
    if share1.size != share2.size:
        messagebox.showerror("Error", "Share images are not the same size.")
        return

    # Create a blank image with the same size as the shares
    width, height = share1.size
    combined_image = Image.new("1", (width, height), 255)

    # Combine the shares using XOR operation
    for x in range(width):
        for y in range(height):
            r1 = share1.getpixel((x, y))
            r2 = share2.getpixel((x, y))
            combined_image.putpixel((x, y), r1 ^ r2)

    # Invert the image vertically
    combined_image = ImageOps.invert(combined_image)

    # Get a filename to save the decrypted image using a file dialog
    save_filename = filedialog.asksaveasfilename(title="Save Decrypted Image", filetypes=[("PNG files", "*.png")])

    # Save the decrypted image
    combined_image.save(save_filename + "_decrypted.png")

    # Display a message box indicating that the image has been decrypted
    messagebox.showinfo("Success", "Image decrypted successfully.")



# Create the main window
root = Tk()

# Create a button to trigger the decryption
decrypt_button = Button(root, text="Decrypt Image", command=decrypt_image)
decrypt_button.pack()

# Start the GUI main loop
root.mainloop()