from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent
DATASET_DIR=BASE_DIR/"dataset"
MODEL_DIR=BASE_DIR/"models"
MODEL_PATH=MODEL_DIR/"mango_mobilenetv2.keras"
UPLOAD_DIR=BASE_DIR/"uploads"
IMAGE_SIZE=(224,224)
BATCH_SIZE=16
EPOCHS=12
SEED=42
CLASSES=["Anthracnose","Bacterial_Canker","Die_Back","Powdery_Mildew","Healthy"]
ALLOWED_EXTENSIONS={"jpg","jpeg","png"}
DISEASE_INFO={
"Anthracnose":{"summary":"A fungal disease that can cause dark, irregular lesions.","care":"Remove affected debris, improve airflow and consult a horticulture expert."},
"Bacterial_Canker":{"summary":"A bacterial disease that may cause dark angular lesions and cankers.","care":"Sanitize tools, avoid moving infected material and seek local extension advice."},
"Die_Back":{"summary":"Shoots or branches progressively dry from the tip backward.","care":"Inspect plant health and drainage; seek expert advice before pruning."},
"Powdery_Mildew":{"summary":"A fungal disease often associated with pale powder-like growth.","care":"Improve canopy airflow and ask a specialist about locally approved management."},
"Healthy":{"summary":"The model found this image most similar to its healthy training class.","care":"Continue regular monitoring; this result cannot rule out every disease."}}
