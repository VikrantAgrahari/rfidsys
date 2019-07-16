from django.shortcuts import render
from .models import Assesment, Subjects

# Create your views here.
def index(request):
    return render(request, 'rfid/index.html')