# Dataset preparation guide

The starter model expects five image classes: Anthracnose, Bacterial_Canker, Die_Back, Powdery_Mildew, Healthy.

Create this directory structure and put real, correctly labeled images in each class folder:
```
dataset/
  train/<class folders>/
  validation/<class folders>/
  test/<class folders>/
```

A starting split is 70% train, 15% validation and 15% test. Keep near-duplicate images and photos from the same source in only one split. Never use test images for training or tuning. Check labels, remove corrupt images and aim for a balanced class count.

Use only a dataset whose license permits your intended use. Record its source and license. If your dataset has different class names, update CLASSES in config.py and keep the same class order for training and inference.

Run python train.py, then python evaluate.py. The best validation-loss model is saved to models/mango_mobilenetv2.keras.

Model quality depends on data quality and independent evaluation. Ask an agricultural specialist to review labels where possible. The prototype is not a certified plant-health diagnosis.
