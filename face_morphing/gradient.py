from PIL import Image
import numpy as np

im1 = Image.open('1.png')
im2 = Image.open('2.png')

while True:
    n = input("Введи число промежуточных стадий\n")
    try:
        n = int(n)
        break
    except:
        print("Число промежуточных стадий - целое число")
        continue

pix_1 = np.array(im1)
pix_2 = np.array(im2)
pix_0 = np.zeros((n,) + pix_1.shape, dtype = int)

m = np.linspace(0, 1, num = n + 2)[1:-1] # num = число картинок + 2

iint = np.vectorize(int) # векторизуем int

for i in range(len(m)):
    pix_0[i] = iint(iint(pix_1) + (iint(pix_2) - iint(pix_1)) * m[i])
    
pix = np.hstack((pix_1, *pix_0, pix_2)).astype(np.uint8) # массив из всех изображений
Image.fromarray(pix).show()
Image.fromarray(pix).save('gradient.png')