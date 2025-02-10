# #USAGE : python test.py

# from keras.models import load_model
# from time import sleep
# from keras.proprocessing.image import img_to_array
# from keras.proprocessing import image
# import cv2
# import numpy as np

# face_classifire = cv2.cascadeclassifier('./haarcascade_frontalface_default.xml')
# classifire =load_model('/Emotion_Detection.h5')

# class_labels = ['Angry','happy','neutral','sad','surprise']

# cap = cv2.videocapture(0)



# while true:
#     # grab a single fram of video
#     ret, fram = cap.reat()
#     labals =[]
#     gray = cv2.rectangle(frame,(x,y),(x+w,y+h),(225,0,0),2)
#     roi_gray = gray[y:+h,x+w]
#     roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AEEA)
    
#     if np.sum([roi_gray])!=0:
#         roi = roi_gray.astype('float')/255.0
#         roi = img_to_array(roi)
#         roi = np.expand_dims(roi,axis=0)
        
#     #make a prediction on the ROI,then lookup the class
    
#         preds =classifire.predict(roi)[0]
#         print("\nprediction=",preds)
#         label=class_labels[preds.argmax()]
#         print("\nprediction max = ",preds.argmax())
#         print("\nlabel = ",label)
#         label_position =(x,y)
#         cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
#     else:
#         cv2.putText(fram,'No Face Found',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
#     PRINT("\n\n")
# cv2.imshow('Emotion Detector',frame)
# if cv2.waitkey(1) & 0xFF == ord('d'):
#     break

a=float(input ("enter the number"))
if a%2==0 and a!=2:
    (print ("it is divisible by 2"))
if a%3==0 and a!=3:
    (print("it is divisible by 3"))
if a%4==0 and a!=4:
    (print("it is divisible by 4"))
if a%5==0 and a!=5:
    (print("it is divisible by 5"))
if a%6==0 and a!=6:
    (print("it is divisible by 6"))
if a%7==0 and a!=7:
    (print("it is divisible by 7"))
if a%8==0 and a!=8:
    (print("it is divisible by 8"))
if a%9==0 and a!=9:
    (print("it is divisible by 9"))
if a%10==0 and a!=10:
    (print("it is divisible by 10"))
if a%11==0 and a!=11:
    (print("it is divisible by 11"))
if a==2 or a==3 or a==5 or a==7 or a==11 or (a%2!=0 and a%3!=0 and a%4!=0 and a%4!=0 and a%5!=0 and a%5!=0 and a%6!=0 and a%7!=0 and a%8!=0 and a%9!=0 and a%9!=0 and a%10!=0 and a%11!=0):
    (print("it is prime number"))

        
                    