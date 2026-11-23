# 🥭 Mango Disease Detector

An educational end-to-end mango leaf image classification project using TensorFlow/Keras transfer learning and a Flask web interface.

## Project status
- Flask upload-and-predict interface and model-training pipeline are provided.
- Dataset folders and preparation instructions are included.
- **Dataset images and trained weights are not included yet.** Add a properly licensed labeled dataset and train before treating predictions as meaningful.
- If model weights are missing, the app displays a setup message instead of inventing a result.

## Features
- Upload JPG, JPEG, and PNG leaf images
- MobileNetV2 transfer-learning training pipeline
- Train/validation/test folder support
- Predicted class and model confidence
- Disease information and general care guidance
- Evaluation script and basic tests
- Responsive web interface

## Classes
Starter labels: Anthracnose, Bacterial Canker, Die Back, Powdery Mildew, Healthy. Ensure your dataset uses these exact folder names, or update `config.py`.

## Structure
```
Mango-Disease-Detector/
├── app.py
├── config.py
├── train.py
├── predict.py
├── evaluate.py
├── requirements.txt
├── README.md
├── templates/index.html
├── static/css/style.css
├── static/js/script.js
├── dataset/{train,validation,test}/<class folders>
├── models/
├── uploads/
├── docs/DATASET_GUIDE.md
└── tests/test_config.py
```

## Windows setup
Install Python 3.10 or 3.11, then run:
```powershell
git clone https://github.com/abhishekgzp234-oss/Mango-Disease-Detector.git
cd Mango-Disease-Detector
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Prepare the dataset using [Dataset Guide](docs/DATASET_GUIDE.md), then train:
```powershell
python train.py
python app.py
```
Open http://127.0.0.1:5000

## Dataset layout
```
dataset/
  train/{Anthracnose,Bacterial_Canker,Die_Back,Powdery_Mildew,Healthy}/
  validation/{Anthracnose,Bacterial_Canker,Die_Back,Powdery_Mildew,Healthy}/
  test/{Anthracnose,Bacterial_Canker,Die_Back,Powdery_Mildew,Healthy}/
```
Use images you have permission to use. Keep test images separate from training and validation.

## Important
This is an educational decision-support prototype, not a certified plant-health diagnostic tool. Image quality, lighting, cultivar, and unseen diseases can affect results. Confirm suspected disease with an agricultural expert. Confidence is a model score, not a guarantee.

## License
Dataset and model licenses must be checked separately. Add a code license only after choosing one.
