import numpy as np 
import matplotlib.pyplot as plt 
import cv2 



def show_mat(image,title,pos):

	image_rgb = image[:,:,::-1]

	ax  = plt.subplot(2,3,pos)
	plt.imshow(image_rgb)
	plt.title(title)
	plt.axis("off")


plt.figure(figsize=(12,6))

image = cv2.imread("lenna.png")




#Make Images Lighter
M = np.ones(image.shape,dtype='uint8') * 60
added_images = cv2.add(image,M)




# Make Images Darker
N = np.ones(image.shape,dtype='uint8') * 60
subtracted_images = cv2.subtract(image,N)


#Scalar 
scalar = np.ones((1,3),dtype='float') * 110
scalar_add = cv2.add(image,scalar)
scalar_subtract  = cv2.subtract(image,scalar)




show_mat(image,"Original Image",1)
show_mat(added_images,"Lighter One",2)
show_mat(subtracted_images,"Darker One",3)
show_mat(scalar_add,"Scalar Added ",5)
show_mat(scalar_subtract,"Scalar Subtracted",6)


plt.show()




