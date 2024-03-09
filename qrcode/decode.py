from pyzbar.pyzbar import decode
from PIL import Image

data = decode(Image.open("output.png"))

print(data)