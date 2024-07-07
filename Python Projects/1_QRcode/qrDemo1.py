# pip install qrcode
import qrcode as qr
img = qr.make("Hello , paste link here.... "); # make creates QR code
img.save("qr.png"); # saves QR image as .png
# default image is store in main working directory