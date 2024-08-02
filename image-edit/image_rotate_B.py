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

#Create an instance of the class
dir_path = "/Users/ijeriomitogun/Projects/DataAnnotations/Python/image-edit"
img_editor = Image_edit(dir_path + '/IMG.jpg')

#Rotate the image by 90 degrees and save the rotated image at 'rotated_image.jpg'
img_editor.rotate_image(90, dir_path + '/B/' + 'rotated_image.jpg')

#Invert the image and save the inverted image at 'inverted_image.jpg' 
img_editor.invert_image(dir_path + '/B/' + 'inverted_image.jpg')

#Convert the image to black and white and save at 'bw_image.jpg'
img_editor.convert_to_black_and_white(dir_path + '/B/' + 'bw_image.jpg')