from django.shortcuts import render,redirect,get_object_or_404
from .models import Image
from .forms import ImageForm
from django.http import JsonResponse
from .tasks import detect_deepfake_task

# Create your views here.
