# Dataset preparation guide

## Recommended public dataset
Use the MangoLeafBD dataset by Ali et al. (2022): https://data.mendeley.com/datasets/hxsnvwty3r/1
It contains 4,000 JPG mango-leaf images across eight balanced classes (500 per class): Anthracnose, Bacterial Canker, Cutting Weevil, Die Back, Gall Midge, Powdery Mildew, Sooty Mould and Healthy.

**License warning:** the dataset is listed under Creative Commons Attribution-NonCommercial 3.0 (CC BY-NC 3.0). Review its terms and cite the dataset authors. Do not use it commercially unless you have separate permission. The images are not copied into this GitHub repository.

## Folder structure
Extract the dataset and split images into:
```
dataset/
  train/<class folders>/
  validation/<class folders>/
  test/<class folders>/
```
The folder names must match CLASSES in config.py exactly:
Anthracnose, Bacterial_Canker, Cutting_Weevil, Die_Back, Gall_Midge, Powdery_Mildew, Sooty_Mould, Healthy.

## Split and quality checks
A practical starting split is 70% train, 15% validation and 15% test. Keep near-duplicate photos and images from the same source in only one split. Never use test images for training or tuning. Check labels, remove corrupt images and aim for balanced classes.

## Train and evaluate
Run python train.py, then python evaluate.py. The best validation-loss model is saved to models/mango_mobilenetv2.keras. Keep a record of the dataset version, split method and test metrics.

Model quality depends on data quality and independent evaluation. Have labels reviewed by an agricultural specialist where possible. This prototype is not a certified plant-health diagnosis.
