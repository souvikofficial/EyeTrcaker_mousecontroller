import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)   # 0 is for enabling cam

face_mesh = mp.solutions.face_mesh.FaceMesh(  refine_landmarks=True   )
screen_w,screen_h = pyautogui.size()

while True :
    ret , frame = cam.read()
    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)   #cvtcolor is convert colour
    output = face_mesh.process(rgb_frame)
    landmark_parts = output.multi_face_landmarks # every point on face
    frame_h,frame_w ,_ = frame.shape # frame height width and dimention

    if landmark_parts :
        landmarks = landmark_parts[0].landmark
        for id,landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x *frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame ,(x,y),3,(0,255,0) ) # cirle(where to draw, center,radious,color)

            if id==1:
                screen_x = screen_w/ frame_w * x
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x,screen_y)
        
            print (x,y)

    left = [landmarks[145],landmarks[159]]
    for landmark in left :
        x = int(landmark.x *frame_w)
        y = int(landmark.y * frame_h)
        cv2.circle(frame ,(x,y),3,(0,255,255) ) # left eye
        
    if(left[0].y - left[1].y) < 0.004 : # difference btw the eye lids coordinate
        pyautogui.click()
        pyautogui.sleep(1)
        
    cv2.imshow("Eye Controlled Mouse", frame)
    cv2.waitKey(1)
