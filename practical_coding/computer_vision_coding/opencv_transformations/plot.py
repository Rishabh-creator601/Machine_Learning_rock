import matplotlib.pyplot as plt 
import cv2



def show_mat(image,title,pos,plot_values=[2,7]):

	image_rgb = image[:,:,::-1]

	plt.subplot(plot_values[0],plot_values[1],pos)
	plt.imshow(image_rgb)
	plt.title(title)
	plt.axis("off")



def to_bgr(image):
	return cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
