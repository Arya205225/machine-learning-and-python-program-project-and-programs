import qrcode
fron PIL import image
qr=qrcode.Qrcode(version=1,error,correction=qrcode.constants.error_correct_H,box size=10,border=4,)
qr.add_data("https://www.linkedin.com/in/aryan-raj-4251b0290")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="green")
img.save("qrlinked.jpg")
