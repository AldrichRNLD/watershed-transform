import numpy as np
from Watershed import Watershed
from PIL import Image
import matplotlib.pyplot as plt

w = Watershed()
image = np.array(Image.open('pic.png')) #fotonya
labels = w.apply(image)
plt.imshow(labels, cmap='Paired', interpolation='nearest')
plt.show()