import matplotlib.pyplot as plt 
import numpy as np 
import cv2 











def to_bgr(image):
	return cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)


def to_gray(image):
	return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


def to_rgb(image):
	return image[:,:,::-1]



def make_lighter(image,light_rate=60):

	M = np.ones(image.shape,dtype='uint8') * light_rate
	image = cv2.add(image,M)

	return image 



def make_darker(image,dark_rate=60):
	M = np.ones(image.shape,dtype='uint8') * dark_rate
	image = cv2.subtract(image,M)

	return image 




def sketch_image(image,ksize=5,return_thresh=False):

	image = to_gray(image)

	image = cv2.medianBlur(image,5)

	edges = cv2.Laplacian(image,cv2.CV_8U,ksize=ksize)

	ret,threshold  = cv2.threshold(edges,60,255,cv2.THRESH_BINARY_INV)

	image_new =to_bgr(threshold)

	if return_thresh == True:
		return threshold

	return image_new




def cartoonize(image):

	threshold  =  sketch_image(image,return_thresh=True)
	filtered = cv2.bilateralFilter(image,10,250,250)
	image_new = cv2.bitwise_and(filtered,filtered,mask=threshold)

	return image_new





def plot_single(image,title):



	image = to_rgb(image)

	plt.imshow(image)
	plt.title(title)
	plt.show()



def plot_mat(image,title,pos,values=[2,5]):


	""" Use plt.figure() before this function and plt.show() after this """

	image = to_rgb(image)

	plt.subplot(values[0],values[1],pos)
	plt.imshow(image)
	plt.title(title)
	plt.axis("off")

