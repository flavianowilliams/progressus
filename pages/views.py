from django.shortcuts import render

# Create your views here.

def HomePageDetail(request):
    return render(request, 'pages/index.html')