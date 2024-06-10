from django.urls import path
from .views import upload_file, visualize

urlpatterns = [
    path('', upload_file, name='home'),
    path('upload/', upload_file, name='upload_file'),
    path('visualize/', visualize, name='visualize'),
]
