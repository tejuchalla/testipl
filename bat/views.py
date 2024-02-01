from django.shortcuts import render

# Create your views here.
def batpage(req):
    return render(req,'batpage.html')
