import qrcode

def genQrCode(text, fileName):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=3
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='green', back_color='white')
    img.save(fileName)

# Main block
if __name__ == '__main__':
    text = 'https://github.com/ian-kinyanjui-ndungu'
    fileName = 'gitProfLink.png'  # Include file extension
    genQrCode(text, fileName)
    print(f'Here is your QR code: {fileName}')
