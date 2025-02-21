#Web-cam.
import cv2

cam = cv2.VideoCapture(0)  #this statement ensures that we are starting our web-cam.
#cv2.nameWindow("web-cam")

img_counter = 0
while True:
	ret,frame = cam.read()
	if not ret:
		print("failed to grab frame")
		break
	cv2.imshow("Web-cam2.O",frame)  #this statement ensues that we are showing the frame to the user
	
	k = cv2.waitKey(1)
	if k % 256 == 27:
		print("")
		break
	elif k % 256 == 32:
		img_name = "opencv_frame_{}.png".format(img_counter)
		cv2.imwrite(img_write,frame)
		print("Screenshot taken")
		img_counter += 1

cam.release()  #it releases the web-cam
cam.destroyALLWindows()
