import qrcode

data = "https://muirurivivian.github.io"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(r"v:\Side\Wangui\qrcode.png")
print("QR Code generated successfully at v:\\Side\\Wangui\\qrcode.png")
