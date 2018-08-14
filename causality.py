import numpy as np
import cv2
import collections as col

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('vtest.mp4')

prev_frames = col.deque(range(20))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.avi', fourcc, 20.0,(640,480))

while(True):
#while(cap.isOpened()):
    ret, frame = cap.read()
    #frame[:100][:100] = [255,100,0]
    #print(frame[0][0])
    kernel=np.array([[0,-1,0],[-1,50,-1],[0,-1,0]])
    gauss_kernel = np.array([[0.3,0.3,0.3],[0.3,0.3,0.3],[0.3,0.3,0.3]])
    frame2show = prev_frames[-1]+frame-100
    frame2show = cv2.filter2D(frame2show,-1,kernel)
    frame2show = frame2show+prev_frames[-1]
    #frame2show = frame2show+(frame2show%prev_frames[-2])
    frame2show = cv2.filter2D(frame2show,-1,gauss_kernel)-(frame2show)
    frame2show = cv2.filter2D(frame2show,-1,kernel)
    prev_frames.appendleft(frame+frame2show)
    prev_frames.pop()
   
    frame2show = cv2.bitwise_not(frame2show)

    cv2.imshow('frame', frame2show)
    out.write(frame2show)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
