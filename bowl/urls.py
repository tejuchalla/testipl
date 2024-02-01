from django.urls import path
from bowl.views import bowlpage

urlpatterns = [
    path('bowler/',bowlpage),

]
