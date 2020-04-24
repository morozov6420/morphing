import numpy as np
from PIL import Image, ImageDraw 

k = 20
# Координаты точек первого кадра
x_1  = np.array((
    8*k,        # 0я точка левое плечо
    8*k + 3*k,  # 1я точка центр шеи
    8*k + 6*k,  # 2я точка правое плечо
    8*k + 2*k,  # 3я точка левое бедро
    8*k + 3*k,  # 4я точка центр таза
    8*k + 4*k,  # 5я точка правое бедро
    8*k,        # 6я точка левая рука
    8*k + 6*k,  # 7я точка правая рука
    8*k + 2*k,  # 8я точка левая нога
    8*k + 4*k   # 9я точка правая нога
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
x_2[6] = 8*k - 3*k # шевелим левой рукой
y_2[6] = 8*k - 3*k # шевелим левой рукой
# Третий кадр
x_3 = x_2.copy()
y_3 = y_2.copy()
x_3[7] = 8*k + 9*k # шевелим правой рукой
y_3[7] = 8*k - 3*k # шевелим правой рукой
# Четвёртый кадр
x_4 = x_3.copy()
y_4 = y_3.copy()
x_4[6] = 8*k - 5*k # шевелим обоими руками
x_4[7] = 8*k + 11*k # шевелим обоими руками
y_4[6] = 8*k # шевелим обоими руками
y_4[7] = 8*k # шевелим обоими руками
# Все кадры
x_set = np.array((x_1, x_2, x_3, x_4, x_1)).T
y_set = np.array((y_1, y_2, y_3, y_4, y_1)).T
# Создаём промежуточные кадры
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

# соединения точек в линии
line_seq = [
    [0, 1], # нулевая с первой
    [1, 2], # первая со второй и тд
    [0, 6], [1, 4], [2, 7], [3, 4], [4, 5], [3, 8], [5, 9]] 
gif = []
for i in range(len(xx[0])):
    l = []
    for d in line_seq:
        l.append(np.array(([xx[d[0]][i], yy[d[0]][i]], [xx[d[1]][i], yy[d[1]][i]])))
    # Координаты головы
    ellip = [(10*k, 5*k), (12*k, 7*k)]
    # Создаём поле для кадра
    img = Image.new('RGB', (22*k, 29*k), 'white') 
    img1 = ImageDraw.Draw(img)
    # Рисуем голову
    img1.ellipse(ellip, fill = "white", outline = "red", width = 3)
    # Рисуем все линии
    for j in l:
        img1.line(list(map(tuple, j)), fill = "red", width = 3)
    # Добавляем кадр в массив
    gif.append(img)
    # Сохраняем кадр
    img.save('frames/frame' + str(i) + '.png')
# Сохраняем анимацию
gif[0].save(
    'dance.gif', format = 'GIF', append_images = gif[1:], 
    save_all=True, duration=120, loop=0
)
