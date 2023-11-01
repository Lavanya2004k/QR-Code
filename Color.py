import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=5,)
qr.add_data("https://www.linkedin.com/in/kotha-lavanya-15a37b235/")
qr.make(fit=True)
img=qr.make_image(fill_color="green",back_color="black")
img.save("LavanyaProfile.png")