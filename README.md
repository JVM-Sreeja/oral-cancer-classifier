Oral Cancer Classifier

A Django-based web application that uses a **Vision Transformer (ViT)** deep learning model to classify oral images as **Cancer** or **Non Cancer**.

Features:
* Image upload through a Django web interface
* Deep learning classification using Vision Transformer (ViT)
* Binary classification:
  * Cancer
  * Non Cancer

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

Setup:(cmd)
Clone the repository:
git clone https://github.com/JVM-Sreeja/oral-cancer-classifier.git

Go to the project folder:
cd oral-cancer-classifier

Create a virtual environment:
python -m venv venv

Activate the virtual environment:
venv\Scripts\activate

Install the required packages:
pip install -r requirements.txt

Model
The project uses a pretrained Vision Transformer architecture:
vit_base_patch16_224`
The model is configured for two classes:
* Cancer
* Non Cancer
The trained model file is:`oralcancer_vit.pth`
The model file is not included in this repository because of its large file size.
For local use, make sure the path used in `classifier/predict.py` points to the correct model location. A project-relative path is recommended instead of a computer-specific path.

Run Locally
Start the Django development server: python manage.py runserver
The application can then be accessed through the local Django development server.

Note:This project is intended for **educational and demonstration purposes**. It is not a medical diagnostic tool and should not be used as a substitute for professional medical diagnosis or clinical evaluation.
