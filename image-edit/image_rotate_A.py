import numpy as np
from PIL import Image, ImageOps


class Image_edit:
    def __init__(self, image_path):
        self.image_path = image_path
        self.img = Image.open(self.image_path)
        self.width, self.height = self.img.size

    def rotate_image(self, angle, save_path):
        #rotate the image
        self.rotated_img = self.img.rotate(angle, expand=1)
        self.rotated_img.save(save_path)
        print(f"Image rotated by {angle} degrees and saved at {save_path}")

    def invert_image(self, save_path):
        #invert the image
        inverted_img = ImageOps.invert(self.img.convert('RGB'))
        inverted_img.save(save_path)
        print(f"Image inverted and saved at {save_path}")  

    def convert_to_black_and_white(self, save_path):
        #convert to grayscale
        grayscale_img = self.img.convert('L')
        #convert to black and white
        bw_img = grayscale_img.point(lambda x: 0 if x<128 else 255, '1')
        bw_img.save(save_path) 
        print(f"Image converted to black and white and saved at {save_path}")        

 #Example usage:
dir_path = '/Users/ijeriomitogun/Projects/DataAnnotations/Python/image-edit'
image_path = dir_path + '/IMG.jpg'
edit = Image_edit(image_path)
angle = 90

save_path = dir_path + '/A/rotated_image.jpg'
edit.rotate_image(angle, save_path)
save_path = dir_path + '/A/inverted_image.jpg'
edit.invert_image(save_path)
save_path = dir_path + '/A/bw_image.jpg'
edit.convert_to_black_and_white(save_path)