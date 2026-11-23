# 🥭 Mango Disease Detector

An educational end-to-end mango leaf image classification project using TensorFlow/Keras transfer learning and a Flask web interface.

## Project status
- Flask upload-and-predict interface and MobileNetV2 training pipeline are included.
- Eight class-specific dataset folder structures and preparation instructions are included.
- **Dataset images and trained weights are not bundled.** Download the dataset separately, follow its license, prepare the splits and train before using predictions.
- If model weights are missing, the app displays a setup message instead of inventing a result.

## Classes
Anthracnose, Bacterial Canker, Cutting Weevil, Die Back, Gall Midge, Powdery Mildew, Sooty Mould and Healthy. These match the MangoLeafBD eight-class dataset family. See docs/DATASET_GUIDE.md for source and license notes.

## Structure
```
Mango-Disease-Detector/
├── app.py, config.py, train.py, predict.py, evaluate.py
├── requirements.txt
├── templates/index.html
├── static/css/style.css
├── static/js/script.js
├── dataset/{train,validation,test}/<8 class folders>/
├── models/
├── uploads/
├── docs/DATASET_GUIDE.md
└── tests/test_config.py
```

## Windows setup
Install Python 3.10 or 3.11, then:
```powershell
git clone https://github.com/abhishekgzp234-oss/Mango-Disease-Detector.git
cd Mango-Disease-Detector
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Download and prepare the dataset as described in the [Dataset Guide](docs/DATASET_GUIDE.md), then run:
```powershell
python train.py
python evaluate.py
python app.py
```
Open http://127.0.0.1:5000

## Dataset layout
Each of train, validation and test must contain these folders: Anthracnose, Bacterial_Canker, Cutting_Weevil, Die_Back, Gall_Midge, Powdery_Mildew, Sooty_Mould, Healthy. Use a separate test set.

## Important
This is an educational decision-support prototype, not a certified plant-health diagnostic tool. Image quality, lighting, cultivar, and unseen diseases can affect results. Confirm suspected disease with an agricultural expert. Confidence is a model score, not a guarantee.

## Dataset attribution
The MangoLeafBD dataset is described by Ali et al. (2022), DOI: 10.17632/hxsnvwty3r.1. Check the dataset's non-commercial Creative Commons license before reuse. Dataset images are not redistributed in this repository.

## License
Dataset and model licenses must be checked separately. Add a code license only after choosing one.
