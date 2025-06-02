import cv2,time,os

video_path =  os.path.join("C:/logs/LAB/test_.avi")

capture = cv2.VideoCapture(0)



frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_fps = capture.get(cv2.CAP_PROP_FPS)



fourcc  = cv2.VideoWriter_fourcc('X','V','I','D')

output = cv2.VideoWriter(video_path,fourcc,int(frame_fps),(int(frame_width),int(frame_height)),False)



print("Frame Width  : {} ".format(frame_width))
print("Frame Height : {} ".format(frame_height))
print("Frame FPS : {} ".format(frame_fps))



frame_index = 0 


while capture.isOpened():

	ret,frame = capture.read()


	if ret is True:


		#cv2.imshow("Input Frame ",frame)


		


		gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

		cv2.imshow("Gray Input Frame",gray_frame)


		output.write(gray_frame)



		if cv2.waitKey(1) & 0xFF == ord("q"):
			break


		if cv2.waitKey(1) & 0xFF == ord("c"):
			frame_name = "frame_{}.png".format(frame_index)

			cv2.imwrite(frame_name,frame)
			frame_index += 1






	else:
		break 



capture.release()
cv2.destroyAllWindows()






