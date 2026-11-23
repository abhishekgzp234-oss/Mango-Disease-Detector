import tensorflow as tf
from config import DATASET_DIR,MODEL_PATH,IMAGE_SIZE,BATCH_SIZE,CLASSES
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
def main():
 if not MODEL_PATH.exists(): raise FileNotFoundError("Run python train.py first.")
 folder=DATASET_DIR/"test"
 if not folder.exists(): raise FileNotFoundError("Missing dataset/test")
 ds=tf.keras.utils.image_dataset_from_directory(folder,labels="inferred",label_mode="categorical",class_names=CLASSES,image_size=IMAGE_SIZE,batch_size=BATCH_SIZE,shuffle=False).map(lambda x,y:(preprocess_input(x),y))
 model=tf.keras.models.load_model(MODEL_PATH)
 print(model.evaluate(ds,return_dict=True))
 print("Class order:",CLASSES)
if __name__=="__main__": main()
