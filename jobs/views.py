from django.shortcuts import render

from .models import Job

def home(Request):
    Jobs = Job.objects
    return render(Request, 'Jobs/home.html', {'Jobs': Jobs})
