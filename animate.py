import numpy as np
from PIL import Image, ImageDraw 

k = 20
# Координаты первого кадра
x_1  = np.array((
    8*k,        # 0
    8*k + 3*k,  # 1
    8*k + 6*k,  # 2
    8*k + 2*k,  # 3
    8*k + 3*k,  # 4
    8*k + 4*k,  # 5
    8*k,        # 6
    8*k + 6*k,  # 7
    8*k + 2*k,  # 8
    8*k + 4*k   # 9
))
y_1 = np.array((
    8*k,        # 0
    8*k,        # 1
    8*k,        # 2
    8*k + 6*k,  # 3
    8*k + 6*k,  # 4
    8*k + 6*k,  # 5
    8*k + 7*k,  # 6
    8*k + 7*k,  # 7
    8*k + 13*k, # 8
    8*k + 13*k  # 9
))
# Второй кадр
x_2 = x_1.copy()
x_2[6] = 8*k - 3*k
y_2 = y_1.copy()
y_2[6] = 8*k - 3*k
# Третий кадр
x_3 = x_2.copy()
y_3 = y_2.copy()
x_3[7] = 8*k + 9*k
y_3[7] = 8*k - 3*k
# Четвёртый кадр
x_4 = x_3.copy()
y_4 = y_3.copy()
x_4[6] = 8*k - 5*k
x_4[7] = 8*k + 11*k
y_4[6] = 8*k
y_4[7] = 8*k

x_set = np.array((x_1, x_2, x_3, x_4, x_1)).T
y_set = np.array((y_1, y_2, y_3, y_4, y_1)).T

x = []
xx = []
y = []
yy = []

for i in range(len(x_set)):
    for j in range(len(x_set[i]) - 1):
        x += np.linspace(x_set[i, j], x_set[i, j + 1], num=5, endpoint=False).tolist()
        y += np.linspace(y_set[i, j], y_set[i, j + 1], num=5, endpoint=False).tolist()
    else:
        x += [x_set[i][-1]]
        y += [y_set[i][-1]]
    xx.append(x)
    yy.append(y)
    x = []
    y = []

p = np.array((xx, yy))

gif = []
for i in range(len(p[0][0])):

    l = []
    l.append(np.array(([p[0][0][i], p[1][0][i]], [p[0][1][i], p[1][1][i]])))
    l.append(np.array(([p[0][1][i], p[1][1][i]], [p[0][2][i], p[1][2][i]])))
    l.append(np.array(([p[0][0][i], p[1][0][i]], [p[0][6][i], p[1][6][i]])))
    l.append(np.array(([p[0][1][i], p[1][1][i]], [p[0][4][i], p[1][4][i]])))
    l.append(np.array(([p[0][2][i], p[1][2][i]], [p[0][7][i], p[1][7][i]])))
    l.append(np.array(([p[0][3][i], p[1][3][i]], [p[0][4][i], p[1][4][i]])))
    l.append(np.array(([p[0][4][i], p[1][4][i]], [p[0][5][i], p[1][5][i]])))
    l.append(np.array(([p[0][3][i], p[1][3][i]], [p[0][8][i], p[1][8][i]])))
    l.append(np.array(([p[0][5][i], p[1][5][i]], [p[0][9][i], p[1][9][i]])))

    ellip = [(10*k, 5*k), (12*k, 7*k)]

    img = Image.new('RGB', (22*k, 29*k), 'white') 
    img1 = ImageDraw.Draw(img)
    img1.ellipse(ellip, fill ="white", outline ="red", width = 3)
    for j in l:
        img1.line(list(map(tuple, j)), fill="red", width = 3)
    gif.append(img)

gif[0].save('dance.gif', format='GIF', append_images=gif[1:], save_all=True, duration=120, loop=0)
