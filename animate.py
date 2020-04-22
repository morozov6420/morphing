import numpy as np
from PIL import Image, ImageDraw 

# creating new Image object 
k = 20
img = Image.new('RGB', (22*k, 29*k), 'white') 



x_1  = np.array((8*k + 6*k, 8*k + 3*k, 8*k , 8*k + 4*k, 8*k + 3*k, 8*k + 2*k, 8*k + 6*k, 8*k, 8*k + 4*k, 8*k + 2*k))
y_1 = np.array((8*k, 8*k, 8*k, 8*k + 6*k, 8*k + 6*k, 8*k + 6*k, 8*k + 7*k, 8*k + 7*k, 8*k + 13*k, 8*k + 13*k))
# print(x_1, '\n', y_1)

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







# p1 = np.array((8*k + 6*k, 8*k       ))
# p2 = np.array((8*k + 3*k, 8*k       ))
# p3 = np.array((8*k      , 8*k       ))
# p4 = np.array((8*k + 4*k, 8*k + 6*k ))
# p5 = np.array((8*k + 3*k, 8*k + 6*k ))
# p6 = np.array((8*k + 2*k, 8*k + 6*k ))
# p7 = np.array((8*k + 6*k, 8*k + 7*k ))
# p8 = np.array((8*k      , 8*k + 7*k ))
# p9 = np.array((8*k + 4*k, 8*k + 13*k))
# p10 =np.array((8*k + 2*k, 8*k + 13*k))

# l1 = np.array((p1, p2))
# l2 = np.array((p2, p3))
# l3 = np.array((p1, p7))
# l4 = np.array((p2, p5))
# l5 = np.array((p3, p8))
# l6 = np.array((p4, p5))
# l7 = np.array((p5, p6))
# l8 = np.array((p4, p9))
# l9 = np.array((p6, p10))

# head = np.array((11*k, 6*k))

ellip = [(10*k, 5*k), (12*k, 7*k)] 

img1 = ImageDraw.Draw(img)
img1.ellipse(ellip, fill ="white", outline ="black", width = 3) # левая верхняя и правая нижняя точки
for i in l:
    img1.line(list(map(tuple, i)), fill="red", width = 3)
# img1.line(list(map(tuple, l2)), fill="black", width = 3)
# img1.line(list(map(tuple, l3)), fill="black", width = 3)
# img1.line(list(map(tuple, l4)), fill="black", width = 3)
# img1.line(list(map(tuple, l5)), fill="black", width = 3)
# img1.line(list(map(tuple, l6)), fill="black", width = 3)
# img1.line(list(map(tuple, l7)), fill="black", width = 3)
# img1.line(list(map(tuple, l8)), fill="black", width = 3)
# img1.line(list(map(tuple, l9)), fill="black", width = 3) 


img.show() 
img.save("new1.png")
