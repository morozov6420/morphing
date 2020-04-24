import numpy as np
from PIL import Image, ImageDraw 

k = 20
# first frame coordinates
x_1  = np.array((
    8*k,        # 0 point left плечо
    8*k + 3*k,  # 1 point neck
    8*k + 6*k,  # 2 point right shoulder
    8*k + 2*k,  # 3 point left hip
    8*k + 3*k,  # 4 point 
    8*k + 4*k,  # 5 point right hip
    8*k,        # 6 point left hand
    8*k + 6*k,  # 7 point правая hand
    8*k + 2*k,  # 8 point left leg
    8*k + 4*k   # 9 point правая leg
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
y_2 = y_1.copy()
x_2[6] = 8*k - 3*k # move left hand
y_2[6] = 8*k - 3*k # move left hand
# x_2[9] = 8*k + 6*k # move right leg
# Третий кадр
x_3 = x_2.copy()
y_3 = y_2.copy()
x_3[7] = 8*k + 9*k # move right hand
y_3[7] = 8*k - 3*k # move right hand
# x_3[9] = 8*k + 8*k # move right leg
# Четвёртый кадр
x_4 = x_3.copy()
y_4 = y_3.copy()
x_4[6] = 8*k - 5*k # move both hands
x_4[7] = 8*k + 11*k # move обоими hands
y_4[6] = 8*k # move обоими hands
y_4[7] = 8*k # move обоими hands
# x_4[9] = 8*k + 6*k # move right leg

# all frames
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

# connecting dots in a line
line_seq = [
    [0, 1], #zero with first
    [1, 2], # first with second etc
    [0, 6], [1, 4], [2, 7], [3, 4], [4, 5], [3, 8], [5, 9]] 
gif = []
for i in range(len(xx[0])):
    l = []
    for d in line_seq:
        l.append(np.array(([xx[d[0]][i], yy[d[0]][i]], [xx[d[1]][i], yy[d[1]][i]])))
    # head
    ellip = [(10*k, 5*k), (12*k, 7*k)]
    # empty white frame
    img = Image.new('RGB', (22*k, 29*k), 'white') 
    img1 = ImageDraw.Draw(img)
    # drawing head
    img1.ellipse(ellip, fill = "white", outline = "red", width = 3)
    # drawing all lines
    for j in l:
        img1.line(list(map(tuple, j)), fill = "red", width = 3)
    # add frame to the list
    gif.append(img)
    # save the frame
    img.save('frames0/frame' + str(i) + '.png')
# save the gif
gif[0].save(
    'dance.gif', format = 'GIF', append_images = gif[1:], 
    save_all=True, duration=120, loop=0
)
