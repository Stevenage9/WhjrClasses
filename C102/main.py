from tkinter import image_names
import cv2
import dropbox
import time
import random
from password_generator import PasswordGenerator

pwo = PasswordGenerator()
pwo.excludeschars="#><%*&{}?/\$+!`'|\"=@"

start_time=time.time()
def take_snapshot():
    number=pwo.generate()
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        imagename="capture"+(number)+".png"
        cv2.imwrite(imagename,frame)
        result=False
    return imagename
    print("Image captured successfully")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(imagename):
    access_token="***"
    file=imagename
    file_from=file
    file_to="/whjr/"+imagename
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File successfully uploaded")

def main():
    while True:
        if((time.time() - start_time)>=5):
            name=take_snapshot()
            upload_file(name)
main()