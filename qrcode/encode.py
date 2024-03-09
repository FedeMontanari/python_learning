import qrcode;

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data("Suki yo, anata ga. Koroshitai hodo")
qr.make(fit=True)

img = qr.make_image(back_color="white", fill_color="black")

img.save("output.png")