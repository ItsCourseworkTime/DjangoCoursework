from django.urls import path
from . import views

urlpatterns = [
    path('', views.cvhome, name='cvhome'),
    path('edit/', views.cvedit, name='cvedit'),
]