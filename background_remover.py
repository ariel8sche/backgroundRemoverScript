from rembg import remove
from PIL import Image
image_input = Image.open("C:\\Users\\ariel\\Desktop\\background_remover\\input_path.jpg")
output = remove(image_input)
output.save("C:\\Users\\ariel\\Desktop\\background_remover\\output_path.png")