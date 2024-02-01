from django.shortcuts import render

# Create your views here.
def bowlpage(req):
    return render(req,'bowlpage.html')
