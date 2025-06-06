from PIL import Image 
import os, sys 

ASCII_CHARS = ["@", "x", "Z", "%", "?", "*", "+", ";", ":", ",", ".", " "]
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYX"


def resize_image(image, new_width=100):
  width, height = image.size
  ratio = height/width 
  new_height = int(new_width * ratio)
  resized_image = image.resize((new_width, new_height))
  return resized_image


def grayscale(image):
  # L is pillow's 8-bit pixels grayscal mode 
  grayscaled_image = image.convert("L")
  return grayscaled_image

def pixels_to_ascii(image):
  pixels = image.getdata()
  # apply floor division
  chars = "".join(ASCII_CHARS[pixel//25] for pixel in pixels)
  return chars 

'''Tutorial from: https://github.com/kiteco/python-youtube-code'''
def generate_ascii():
  path = "./static/bootmod2.png"

  try:
    image = Image.open(path)
  except:
    print(path, "is not a valid path")

  new_image_data = pixels_to_ascii(grayscale(resize_image(image)))

  pixel_count = len(new_image_data)
  new_width = 100
  ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
  print(ascii_image) 

  with open("ascii_image.txt", "w") as f:
    f.write(ascii_image)

generate_ascii()