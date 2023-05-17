from rembg import remove
from PIL import Image

# Путь до картинки у которой необходимо вырезать фон, расширение jpg
input_path = 'images/image.jpg'
# Путь, куда будет сохранен результат удаления фона
output_path = 'images/image_output.png'

open_image = Image.open(input_path)
output = remove(open_image)

output.save(output_path)