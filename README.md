Oral Cancer Classifier

A Django-based web application that uses a Vision Transformer (ViT) deep learning model to classify oral images as Cancer or Non Cancer.

 Features:
* Upload oral images through a web interface
* AI-based image classification
* Vision Transformer (ViT) model
* Django web application

 Technologies:
* Python 3.11
* Django 5.2.17
* PyTorch 2.5.1
* Torchvision 0.20.1
* Timm 1.0.28
* Pillow

 Project Structure:
oral-cancer-classifier/
├── cancer_webapp/
├── classifier/
├── static/
├── templates/
├── manage.py

Setup:
git clone https://github.com/JVM-Sreeja/oral-cancer-classifier.git
cd oral-cancer-classifier
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Model:
The project uses a trained Vision Transformer model (`oralcancer_vit.pth`).
The trained model is not included in this repository because of its large file size.

Run Locally:
python manage.py runserver
The application can then be accessed through the local Django development server.

 Note:This project is for educational and demonstration purposes and is not a medical diagnostic tool.
