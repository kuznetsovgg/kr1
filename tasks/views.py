from django.shortcuts import render
from django.conf import settings

# Create your views here.

def index(request):
  context = {
      'key': settings.FIREBASE_API_KEY
  }
  return render(request, "index.html", context)