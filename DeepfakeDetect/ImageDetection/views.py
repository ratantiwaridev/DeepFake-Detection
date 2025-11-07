from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


# Create your views here.

def home(request):
    return render(request, 'ImageDetection/home.html')

def index(request):
    return render(request, 'Imagedetection/index.html')

def upload_image_ajax(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        file_url = fs.url(filename)

        # TODO: Replace with model prediction
        result = "Prediction Pending (Model Not Connected Yet)"

        return JsonResponse({'image_url': file_url, 'result': result})

    return JsonResponse({'error': 'Invalid request'}, status=400)
