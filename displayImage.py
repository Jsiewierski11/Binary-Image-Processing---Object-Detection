import cv2
import matplotlib as mp
import matplotlib.pyplot as plt
import skimage
from skimage import img_as_ubyte

def displayImage(filename, cmap, title=None):
    plt.figure()
    plt.imshow(filename, cmap=cmap)
    if title is not None:
        plt.title(title)
    print("Press any button to continue...")
    plt.waitforbuttonpress()
