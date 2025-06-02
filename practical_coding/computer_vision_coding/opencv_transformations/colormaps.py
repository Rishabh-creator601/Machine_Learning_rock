from plot import show_mat ,to_bgr
import matplotlib.pyplot as plt 
import numpy as np 
import cv2 




image = cv2.imread("lenna.png",cv2.IMREAD_GRAYSCALE)

colormaps = ["AUTUMN", "BONE", "JET", "WINTER", "RAINBOW", "OCEAN", "SUMMER", "SPRING", "COOL", "HSV", "HOT", "PINK",
             "PARULA"]



plt.figure(figsize=(12,5))

show_mat(to_bgr(image),"Gray Image",1)



for idx,value in enumerate(colormaps):

    show_mat(cv2.applyColorMap(image,idx),value,idx + 2)

plt.show()