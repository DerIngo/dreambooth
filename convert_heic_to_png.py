from PIL import Image
from pillow_heif import register_heif_opener
import os

input_folder = "input"
output_folder = "output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# Registriere HEIF-Opener
register_heif_opener()


for filename in os.listdir(input_folder):
    if filename.endswith(".heic"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".heic", ".png"))
        
        with Image.open(input_path) as image:
            # HEIC zu RGB
            image = image.convert("RGB")
            
            # Dimensionen berechnen
            width, height = image.size
            new_size = min(width, height)  # Quadratgröße basierend auf der kürzeren Seite
            
            # Mittig zuschneiden
            left = (width - new_size) // 2
            top = (height - new_size) // 2
            right = left + new_size
            bottom = top + new_size
            image = image.crop((left, top, right, bottom))
            
            # Auf 512x512 skalieren
            image = image.resize((512, 512), Image.Resampling.LANCZOS)

            # Speichern
            image.save(output_path, format="PNG")
