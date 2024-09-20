from rembg import remove
from PIL import Image
image_input = Image.open("root\\input_path.jpg")
output = remove(image_input)
output.save("root\\output_path.png")
