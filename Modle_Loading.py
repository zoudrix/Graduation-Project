from keras.models import model_from_json
import numpy as np
import json




class Abnormal_Model(object) :
    
    
    def __init__(self, model_json_file, weights_file) :
        # get model
        with open(model_json_file, 'r') as f :
            model = f.read()
            self.model = model_from_json(model)
        
        self.model.load_weights(weights_file)   
        #self.model._make_predict_function()    
        
    def predict(self, img) :
        preds = self.model.predict(img)
        return preds
