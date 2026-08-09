from django.shortcuts import render
from .predict import predict_image
import os

def classify_image(request):
    result=None
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        path=f'classifier/temp_{image.name}'
        with open(path, 'wb+')as f:
            for chunk in image.chunks():
                f.write(chunk)
        result=predict_image(path)
        os.remove(path)
    return render(request, 'upload.html',{'result':result})