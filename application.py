from flask import Flask, render_template, request,Response
import os
from keras.models import model_from_json
from Modle_Loading import Abnormal_Model
from preprocessing import processing
import cv2
import numpy as np

loaded_model = Abnormal_Model('model.json', 'model.h5')


ALLOWED_EXTENSIONS = {'gif', 'mp4'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'E:/Ai_pro/graduation project/finalproject'
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

def get_Frames(file_path):
    
    X_train=processing(file_path)
    predictions=loaded_model.predict(np.expand_dims(X_train[0],axis=0))
    

    cap=cv2.VideoCapture(file_path)
                
    success=True

    i=0
    counter=0
    predict_lables=predictions
    print(predict_lables)
    suc=[]
    n=0
    while (True):
        
        success,frame=cap.read()
        if not success:
            break
        suc.append(success)
        if counter==10:
            
            i+=1
            if len(predictions)==i:
                i-=1
            predict_lables=loaded_model.predict(np.expand_dims(X_train[i],axis=0))
            
            counter=0
      
        if (predict_lables[0][0] < predict_lables[0][1]):
            b="{:.2f}".format(predict_lables[0][1])
            frame=cv2.putText(frame,f"Abnormal: {b}",(15,25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)   
            print("Abnormal Behaviour with probability")

        else:
            c="{:.2f}".format(predict_lables[0][0])
            frame=cv2.putText(frame,f"Not Abnormal: {c}",(15,25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)  
        counter+=1
        frame = cv2.imencode('.JPEG', frame,[cv2.IMWRITE_JPEG_QUALITY,20])[1].tobytes()
        
        
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['vid_file']
        file_path = os.path.join('Static/media', f.filename)
        f.save(file_path)
        return render_template('table.html', data=os.listdir('./Static/media'))


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':

        video_path = request.form['vid_name']
        videopath= os.path.join('Static/', video_path)
    

    return Response(get_Frames(videopath),mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
