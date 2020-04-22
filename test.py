from PIL import Image, ImageDraw 
# w, h = 220, 190
k = 20

ell = [(200, 100), (240, 140)] 
# (240, 100), (200, 140)
# ell = [(8*k + 4*k, 8*k - 3*k), (8*k + 2*k, 8*k - 1*k)]
# print(shape, ell)
# creating new Image object 
# img = Image.new("RGB", (w, h)) 

img = Image.new('RGB', (22*k, 29*k), 'white') 
  
# create ellipse image 
img1 = ImageDraw.Draw(img)   
img1.ellipse(ell, fill ="#800080", outline ="green") 
img.show() 