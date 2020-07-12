import cv2
import dropbox
import time
import random 
startTime = time.time()

def TakeSnapshot():
    number = random.randint(0 ,100)
    videocapob = cv2.VideoCapture(0 , cv2.CAP_DSHOW)
    result = True 
    while(result): 
        ret,frame=videocapob.read()
        imageName = "img" + str(number) + ".png"
        cv2.imwrite(imageName , frame)
        startTime = time.time()
        result = False

    return imageName
    print('snapshotTaken')
    videocapob.release()
    cv2.destroyAllWindows()

def UploadFile(image_name):
      access_token = '3M53tm-mOzAAAAAAAAAAEUY13oQkFeV9egsrBKoeEttn_fijfGldLpWLnbptB3b6'
      file = image_name
      filefrom = file
      fileto = "/NewFolder/" + (image_name)
      dbx = dropbox.Dropbox(access_token)
      with open(filefrom ,'rb') as f:
          dbx.files_upload(f.read() , fileto , mode = dropbox.files.WriteMode.overwrite)
          print('file_uploaded')

def main():
     while(True):
         if((time.time() - startTime) >= 5):
             name = TakeSnapshot()
             UploadFile(name)

main()
    