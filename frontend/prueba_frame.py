import os
from PIL import Image

LOGO_FILENAME = 'catlogo.png'
logoIm = Image.open(LOGO_FILENAME)
os.makedirs('withLogo', exist_ok=True)

# Loop over all files in the working directory.
for filename in os.listdir():
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue

    im = Image.open(filename)
    width, height = im.size

    # Resize the logo.
    print(f'Resizing logo to fit {filename}...')
    sLogo = logoIm.resize((int(width / 5), int(height / 5)))
    sLogoWidth, sLogoHeight = sLogo.size

    # Add the logo.
    print(f'Adding logo to {filename}...')
    im.paste(sLogo, (width - sLogoWidth, height - sLogoHeight), sLogo)

    # Save changes.
    im.save(os.path.join('withLogo', filename))