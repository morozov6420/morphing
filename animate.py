import numpy as np
from PIL import Image, ImageDraw 

# creating new Image object 
k = 20
img = Image.new('RGB', (22*k, 29*k), 'white') 

# соммент

x_1  = np.array((8*k + 6*k, 8*k + 3*k, 8*k , 8*k + 4*k, 8*k + 3*k, 8*k + 2*k, 8*k + 6*k, 8*k, 8*k + 4*k, 8*k + 2*k))
y_1 = np.array((8*k, 8*k, 8*k, 8*k + 6*k, 8*k + 6*k, 8*k + 6*k, 8*k + 7*k, 8*k + 7*k, 8*k + 13*k, 8*k + 13*k))

p = np.array((x_1, y_1))
l = list()
l.append(np.array(([p[0][0], p[1][0]], [p[0][1], p[1][1]])))
l.append(np.array(([p[0][1], p[1][1]], [p[0][2], p[1][2]])))
l.append(np.array(([p[0][0], p[1][0]], [p[0][6], p[1][6]])))
l.append(np.array(([p[0][1], p[1][1]], [p[0][4], p[1][4]])))
l.append(np.array(([p[0][2], p[1][2]], [p[0][7], p[1][7]])))
l.append(np.array(([p[0][3], p[1][3]], [p[0][4], p[1][4]])))
l.append(np.array(([p[0][4], p[1][4]], [p[0][5], p[1][5]])))
l.append(np.array(([p[0][3], p[1][3]], [p[0][8], p[1][8]])))
l.append(np.array(([p[0][5], p[1][5]], [p[0][9], p[1][9]])))

ellip = [(10*k, 5*k), (12*k, 7*k)]

img1 = ImageDraw.Draw(img)
img1.ellipse(ellip, fill ="white", outline ="black", width = 3)
for i in l:
    img1.line(list(map(tuple, i)), fill="red", width = 3)

img.show() 
img.save("new1.png")
