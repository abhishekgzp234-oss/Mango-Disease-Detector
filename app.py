from flask import Flask,render_template,request,jsonify
from werkzeug.utils import secure_filename
import uuid
from config import UPLOAD_DIR,MODEL_PATH,ALLOWED_EXTENSIONS,DISEASE_INFO
from predict import predict_image
app=Flask(__name__)
app.config["MAX_CONTENT_LENGTH"]=8*1024*1024
UPLOAD_DIR.mkdir(parents=True,exist_ok=True)
def allowed_file(name):
 return "." in name and name.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS
@app.get("/")
def home(): return render_template("index.html")
@app.post("/predict")
def predict():
 image=request.files.get("image")
 if image is None or not image.filename: return jsonify({"error":"Choose an image first."}),400
 if not allowed_file(image.filename): return jsonify({"error":"Only JPG, JPEG and PNG are supported."}),400
 if not MODEL_PATH.exists(): return jsonify({"error":"Model missing. Add dataset images and run python train.py first."}),503
 path=UPLOAD_DIR/(uuid.uuid4().hex+"_"+secure_filename(image.filename))
 image.save(path)
 try:
  result=predict_image(path); result["info"]=DISEASE_INFO.get(result["class_name"],{})
  return jsonify(result)
 except Exception:
  app.logger.exception("Prediction failed")
  return jsonify({"error":"Could not process this image. Check the model and image file."}),500
 finally: path.unlink(missing_ok=True)
if __name__=="__main__": app.run(host="127.0.0.1",port=5000,debug=False)
