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
CLASSES=["Anthracnose","Bacterial_Canker","Cutting_Weevil","Die_Back","Gall_Midge","Powdery_Mildew","Sooty_Mould","Healthy"]
ALLOWED_EXTENSIONS={"jpg","jpeg","png"}
DISEASE_INFO={
"Anthracnose":{"summary":"A fungal disease that can cause dark, irregular lesions on leaves and other plant parts.","care":"Remove affected debris, improve airflow and consult a horticulture expert."},
"Bacterial_Canker":{"summary":"A bacterial disease that may cause dark angular lesions and cankers.","care":"Sanitize tools, avoid moving infected material and seek local extension advice."},
"Cutting_Weevil":{"summary":"Feeding damage associated with the mango leaf-cutting weevil can affect leaf margins and shoots.","care":"Inspect new flush and seek local agricultural guidance for integrated pest management."},
"Die_Back":{"summary":"Shoots or branches progressively dry from the tip backward.","care":"Inspect plant health and drainage; seek expert advice before pruning."},
"Gall_Midge":{"summary":"Gall midge larvae can cause blister-like or gall symptoms on young leaves.","care":"Monitor new flush, remove affected debris where appropriate and consult a local expert."},
"Powdery_Mildew":{"summary":"A fungal disease often associated with pale powder-like growth.","care":"Improve canopy airflow and ask a specialist about locally approved management."},
"Sooty_Mould":{"summary":"A dark fungal coating that commonly develops on honeydew deposited by sap-feeding insects.","care":"Identify and manage the underlying sap-feeding pest with local expert advice."},
"Healthy":{"summary":"The model found this image most similar to its healthy training class.","care":"Continue regular monitoring; this result cannot rule out every disease."}}
