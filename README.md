# QRCodeGenerator

This script generates a QR code for a given text or URL and saves it as an image file. It utilizes the `qrcode` Python library to create customizable QR codes.

---

## Features

- Generates QR codes for any text or URL.
- Allows customization of:
  - **Box size**: Size of each QR code unit.
  - **Border size**: Thickness of the border around the QR code.
  - **Colors**: Customize foreground and background colors.
- Saves the generated QR code as an image file (e.g., PNG).

---

## Requirements

### Python Version
- Python 3.6 or higher.

### Dependencies
- `qrcode`: For generating QR codes.
- `Pillow`: For creating and saving the QR code as an image.

You can install these dependencies using pip:

```bash
pip install qrcode[pil]
```

---

## How to Use

### 1. Clone or Download the Script
Save the script to your local machine as a `.py` file (e.g., `generate_qr.py`).

### 2. Run the Script
Open a terminal or command prompt, navigate to the directory containing the script, and execute:

```bash
python generate_qr.py
```

### 3. Output
The script generates a QR code and saves it in the current working directory with the filename `gitProfLink.png`. It also prints a confirmation message in the terminal:

```
Here’s your QR code: gitProfLink.png
```

---

## Customization
You can modify the following parameters in the script:

- **Text to Encode**: Change the `text` variable in the `if __name__ == '__main__':` block to the desired text or URL.
  ```python
  text = 'https://example.com'
  ```

- **Output Filename**: Set the `fileName` variable to a preferred file name with an appropriate extension (e.g., `.png`, `.jpg`).
  ```python
  fileName = 'custom_qr_code.png'
  ```

- **QR Code Appearance**: Adjust the `box_size`, `border`, `fill_color`, and `back_color` in the `genQrCode` function:
  ```python
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=3
  )
  img = qr.make_image(fill_color='#000000', back_color='#FFFFFF')
  ```

---

## Example Output
The generated QR code will encode the URL: `https://github.com/ian-kinyanjui-ndungu` and save it as `gitProfLink.png`. You can scan the QR code with any QR code scanner, google scan or compatible camera app.

---
