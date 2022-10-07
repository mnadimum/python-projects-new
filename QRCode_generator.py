# import qrcode
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
	box_size=10, border=6,)
	
qr.add_data("https://paymentservices.amazon.com/airlines")
qr.make(fit=True)
img = qr.make_image(fill_color= "black", back_color = "white")
img.save("amazon_web.png")
