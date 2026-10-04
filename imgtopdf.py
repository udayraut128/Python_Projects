from PIL import Image
import os
import re

# Image folder
input_folder = "linuxcommand"

# Output PDF
output_pdf = "linuxcommand.pdf"

# Supported formats
extensions = (".jpg", ".jpeg", ".png", ".webp", ".bmp")

# Get images
files = [
    f for f in os.listdir(input_folder)
    if f.lower().endswith(extensions)
]

# Natural sorting: 1, 2, 3, ... 10, 11
def natural_sort(filename):
    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split(r"(\d+)", filename)
    ]

files.sort(key=natural_sort)

images = []

print("Images will be added in this order:\n")

for file in files:
    path = os.path.join(input_folder, file)

    try:
        image = Image.open(path).convert("RGB")
        images.append(image)

        print(file)

    except Exception as e:
        print(f"Skipped {file}: {e}")

# Create PDF
if images:
    images[0].save(
        output_pdf,
        save_all=True,
        append_images=images[1:]
    )

    print(f"\nPDF created: {output_pdf}")

else:
    print("No images found.")