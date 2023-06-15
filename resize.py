
from PIL import Image
import pytesseract
import os 
os.environ['PATH']+=r" C:\Users\kaifk\lpth\.vscode"
image = Image.open("screenshot.png")
new_width = 1000
new_height = 800
resized_image = image.resize((new_width, new_height))
resized_image.save("output.png")
print(pytesseract.image_to_string(Image.open('output.png')))
