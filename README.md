Oral Cancer Classifier

A Django-based web application that uses a Vision Transformer (ViT) deep learning model to classify oral images as Cancer or Non Cancer.

Features:
*Image upload through a Django web interface
*Deep learning classification using Vision Transformer (ViT)
*Binary classification:Cancer or Non Cancer

 Technologies:
* Python 3.11
* Django 5.2.17
* PyTorch 2.5.1
* Torchvision 0.20.1
* Timm 1.0.28
* Pillow

 Project Structure:
* cancer_webapp/ — Django project configuration
* classifier/ — Image classification application
* static/ — Static files
* templates/ — HTML templates
* models/ — Model files
* manage.py — Django management script

Setup:
->git clone https://github.com/JVM-Sreeja/oral-cancer-classifier.git
->cd oral-cancer-classifier
->python -m venv venv
->venv\Scripts\activate
->pip install -r requirements.txt

Model:
*The project uses a pretrained Vision Transformer architecture:vit_base_patch16_224
*The model is configured for two classes and uses a trained .pth state dictionary for classification.
*The trained model file is:oralcancer_vit.pth
*Make sure the path used in classifier/predict.py points to the correct model location.
*It is recommended to use a project-relative path rather than a computer-specific path.
*The model file is not included in this repository because of its large file size.

Run Locally:
->python manage.py runserver
The application can then be accessed through the local Django development server.

Note:This project is intended for educational and demonstration purposes. It is not a medical diagnostic tool and should not be used as a substitute for professional medical diagnosis or clinical evaluation.
