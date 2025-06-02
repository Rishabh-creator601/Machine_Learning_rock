import cv2 
import numpy as np 
import matplotlib.pyplot as plt 




def to_bgr(image):
	return cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)



def show_mat(image,title,pos):

	image_rgb = image[:,:,::-1]

	plt.subplot(2,4,pos)
	plt.imshow(image_rgb)
	plt.title(title)
	plt.axis("off")




def sketch_image(image,ksize=5,return_thresh=False):


	""" KSIZE :  choose a odd Number and not larger than 31"""


	gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	gray_image = cv2.medianBlur(gray_image,5) # Make it Blur 


	edges = cv2.Laplacian(gray_image,cv2.CV_8U,ksize=ksize)

	ret,threshold = cv2.threshold(edges,60,255,cv2.THRESH_BINARY_INV)

	image_new = cv2.cvtColor(threshold,cv2.COLOR_GRAY2BGR)

	if return_thresh == True: # Used In ANOTHER FUNCTION 
		return threshold
	
	return image_new


def cartoonize_image(image):


	threshold  =  sketch_image(image,return_thresh=True)

	filtered = cv2.bilateralFilter(image,10,250,250)

	cartoonized = cv2.bitwise_and(filtered,filtered,mask=threshold)

	return cartoonized



plt.figure(figsize=(14,6))
image = cv2.imread("lenna.png")



sketch =  sketch_image(image,5)
cartoonized = cartoonize_image(image)

#Same Inbuilt OpenCv Functions 

# _, sketch_cv  = cv2.pencilSketch(image,sigma_s=5, sigma_r=0.1, shade_factor=0.1)
# styled_cv =  cv2.stylization(image,sigma_s=60,sigma_r=0.07)



show_mat(image,"Original Image",1)
show_mat(sketch,"Sketched Image",2)
show_mat(cartoonized,"Cartoonized Image",3)
#show_mat(styled_cv,"StyledBy Opencv",4)



plt.show()

