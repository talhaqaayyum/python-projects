import qrcode

data = "Hello, Thanks for scanning me"

qr = qrcode.make(data)

# Save QR code as PNG file
qr.save("qrcode.png")

print("QR code is generated Successfully.")
