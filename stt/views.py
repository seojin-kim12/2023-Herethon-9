from django.shortcuts import render

# Create your views here.

def stt(request):
    return render(request, "html/stt.html")