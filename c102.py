import dropbox
import cv2
import time
import random

start_time = time.time()
print(start_time)

def takesnapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print("SnapShot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(img_name):
    access_token = "7DwhG6tM_TcAAAAAAAAAATsXTlKUMOSH0IeKt4ZIfO28qhmcRvANjepWWOVzzJ6P"
    file = img_name
    file_from = file
    file_to = "/photo/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f: 
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
def main():
    while(True):
         if ((time.time()- start_time) >= 5):
             name = takesnapshot()
             uploadFile(name)

main()                      
