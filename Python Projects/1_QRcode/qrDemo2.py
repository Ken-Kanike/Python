# Import the qrcode module, which provides a way to generate QR codes
import qrcode 

# Import the Image module from the Python Imaging Library (PIL), which is used to handle image files
from PIL import Image

# Import the constants module from the qrcode module, which provides constants for error correction levels
import qrcode.constants 

# Create a new QRCode object with the specified parameters:
#   - version: The version of the QR code (1 is the smallest, 40 is the largest)
#   - error_correction: The error correction level (in this case, HIGH)
#   - box_size: The size of each "box" in the QR code (in pixels)
#   - border: The width of the border around the QR code (in boxes)
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4);

# Add the data to be encoded in the QR code (in this case, a URL)
qr.add_data("https://www.google.com/");

# Make the QR code, using the added data and the specified parameters
qr.make(fit=True);

# Create an image from the QR code, with the specified fill and background colors
img = qr.make_image(fill_color="blue", back_color="white");

# Save the image to a file named "google.png"
img.save("google.png");
