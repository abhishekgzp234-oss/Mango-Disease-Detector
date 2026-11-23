import json
import tensorflow as tf
from tensorflow.keras import layers,models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from config import DATASET_DIR,MODEL_DIR,MODEL_PATH,IMAGE_SIZE,BATCH_SIZE,EPOCHS,SEED,CLASSES
def load_split(name,shuffle):
 folder=DATASET_DIR/name
 if not folder.exists(): raise FileNotFoundError(f"Missing {folder}; read docs/DATASET_GUIDE.md")
 return tf.keras.utils.image_dataset_from_directory(folder,labels="inferred",label_mode="categorical",class_names=CLASSES,image_size=IMAGE_SIZE,batch_size=BATCH_SIZE,seed=SEED,shuffle=shuffle)
def main():
 tf.keras.utils.set_random_seed(SEED)
 train=load_split("train",True).map(lambda x,y:(preprocess_input(x),y)).prefetch(tf.data.AUTOTUNE)
 val=load_split("validation",False).map(lambda x,y:(preprocess_input(x),y)).prefetch(tf.data.AUTOTUNE)
 base=MobileNetV2(weights="imagenet",include_top=False,input_shape=(*IMAGE_SIZE,3)); base.trainable=False
 inputs=layers.Input(shape=(*IMAGE_SIZE,3)); x=base(inputs,training=False); x=layers.GlobalAveragePooling2D()(x); x=layers.Dropout(.25)(x); outputs=layers.Dense(len(CLASSES),activation="softmax")(x)
 model=models.Model(inputs,outputs); model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])
 MODEL_DIR.mkdir(parents=True,exist_ok=True)
 callbacks=[tf.keras.callbacks.EarlyStopping(patience=3,restore_best_weights=True,monitor="val_loss"),tf.keras.callbacks.ModelCheckpoint(MODEL_PATH,save_best_only=True,monitor="val_loss")]
 history=model.fit(train,validation_data=val,epochs=EPOCHS,callbacks=callbacks)
 (MODEL_DIR/"training_history.json").write_text(json.dumps(history.history,indent=2),encoding="utf-8")
 print("Saved best model to",MODEL_PATH)
if __name__=="__main__": main()
