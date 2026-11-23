import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from config import MODEL_PATH,IMAGE_SIZE,CLASSES
_model=None
def get_model():
 global _model
 if _model is None:
  if not MODEL_PATH.exists(): raise FileNotFoundError("Run python train.py after preparing the dataset.")
  _model=load_model(MODEL_PATH)
 return _model
def predict_image(image_path):
 image=Image.open(image_path).convert("RGB").resize(IMAGE_SIZE)
 array=preprocess_input(np.expand_dims(np.asarray(image,dtype=np.float32),axis=0))
 scores=get_model().predict(array,verbose=0)[0]
 index=int(np.argmax(scores))
 return {"class_name":CLASSES[index],"confidence":round(float(scores[index])*100,2)}
