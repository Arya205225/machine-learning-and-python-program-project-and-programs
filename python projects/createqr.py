import qrcode
img = qrcode.make("https://www.linkedin.com/in/aryan-raj-4251b0290")
img . save("link_qr.png")