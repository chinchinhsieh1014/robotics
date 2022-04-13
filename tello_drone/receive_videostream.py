import cv2

#input "streamon" in "send_command"
pc = 'udp://@0.0.0.0:11111'
cap = cv2.VideoCapture(pc)

#get the width
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#get the height
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#save the video
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0,(w,h))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
	cap.release()
	#out.release()
	cv2.destroyAllWindows()
        break
