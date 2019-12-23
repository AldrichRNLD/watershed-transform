# watershed-transform

code yg simpel (namun tidak bisa cepat) implementasi via kode python untuk "Determining watersheds in digital pictures via flooding simulations"


thanks ! terima kasih ! :)




konten :
------------------
import numpy as np
from Watershed import Watershed
from PIL import Image
import matplotlib.pyplot as plt

w = Watershed()
image = np.array(Image.open('ex.png'))
labels = w.apply(image)
plt.imshow(labels, cmap='Paired', interpolation='nearest')
plt.show()
