from django.urls import path
from bat.views import batpage

urlpatterns = [
    path('batsman/',batpage),

]
