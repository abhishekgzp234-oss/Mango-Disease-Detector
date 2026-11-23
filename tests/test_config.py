from config import CLASSES,ALLOWED_EXTENSIONS,IMAGE_SIZE
def test_classes_are_unique():
 assert len(CLASSES)==8 and len(set(CLASSES))==8
def test_image_settings():
 assert IMAGE_SIZE==(224,224)
 assert {"jpg","jpeg","png"}.issubset(ALLOWED_EXTENSIONS)
