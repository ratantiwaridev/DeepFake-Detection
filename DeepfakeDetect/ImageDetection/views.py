from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage


# Create your views here.

def home(request):
    return render(request, 'ImageDetection/home.html')

def index(request):
    return render(request, 'Imagedetection/index.html')

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        # You’ll later call your CNN model here to classify fake/real
        result = "Prediction pending"  

        return render(request, 'Imagedetection/result.html', {
            'uploaded_file_url': uploaded_file_url,
            'result': result
        })
    return render(request, 'Imagedetection/upload.html')
