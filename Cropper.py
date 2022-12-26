try:
    from PIL import Image
except ImportError:
    pass

class Cropp:
    
    def crop1(top, bottom, left, right, save_mode, files):

        for file in files:

            if file.endswith('.jpg'):
                ext = 'jpg'
                path = file.rstrip(".jpg")
            elif file.endswith('.png'):
                ext = 'png'
                path = file.rstrip(".png")

            im = Image.open(file)
            cropped = im.crop((left, top, right, bottom))

            if save_mode == "New Save":
                if ext == 'jpg':
                    cropped = cropped.save(f"{path}_cropped.jpg")
                elif ext == 'png':
                    cropped = cropped.save(f"{path}_cropped.png")
            elif save_mode == "Overwrite":
                if ext == 'jpg':
                    cropped = cropped.save(f"{path}.jpg")
                elif ext == 'png':
                    cropped = cropped.save(f"{path}.png")
