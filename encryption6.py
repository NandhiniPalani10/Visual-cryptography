from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageDraw
import random


# Function to handle button click
def encrypt_image():
    # Get the filename of the secret image using a file dialog
    secret_image_filename = filedialog.askopenfilename(title="Select Secret Image", filetypes=[("PNG files", "*.png")])

    # Load the secret image
    secret_image = Image.open(secret_image_filename)

    # Convert the secret image to black and white
    secret_image = secret_image.convert("1")

    # Create two blank images with the same size as the secret image
    width, height = secret_image.size
    share1 = Image.new("1", (width, height), 255)
    share2 = Image.new("1", (width, height), 255)

    # Generate a random pixel pattern for each share
    for x in range(width):
        for y in range(height):
            # For each pixel, generate a random number between 0 and 1
            r1 = random.randint(0, 1)
            r2 = random.randint(0, 1)

            # If the pixel in the secret image is white (0), the pixels in the shares should be opposite
            if secret_image.getpixel((x, y)) == 0:
                share1.putpixel((x, y), r1)
                share2.putpixel((x, y), r1 ^ 1)  # XOR operation to make the shares opposite
            # If the pixel in the secret image is black (1), the pixels in the shares should be the same
            else:
                share1.putpixel((x, y), r1)
                share2.putpixel((x, y), r1 ^ r2) # XOR operation to combine the shares
        
        # Get a filename to save the share images using a file dialog
    save_filename = filedialog.asksaveasfilename(title="Save Share Images", filetypes=[("PNG files", "*.png")])

    # Save the shares and the combined image
    share1.save(save_filename + "_share1.png")
    share2.save(save_filename + "_share2.png")

    # Display a message box indicating that the image has been encrypted
    messagebox.showinfo("Success", "Image encrypted successfully.")

root = Tk()

encrypt_button = Button(root, text="Encrypt Image", command=encrypt_image)
encrypt_button.pack()

#I've added the XOR operation in two places - first to make the shares opposite for white pixels in the secret image, and second to combine the shares for black pixels in the secret image. The `^` operator in Python performs the XOR operation between two bits.
root.mainloop()