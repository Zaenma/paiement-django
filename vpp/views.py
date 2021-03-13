from django.shortcuts import render

def page_404(request):
    return render(request,'404.html')