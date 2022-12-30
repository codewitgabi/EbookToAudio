from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name= "index"),
    # path("read-file/", views.read_file, name= "read_file"),
    path("save-audio/", views.save_audio, name= "save_audio_url"),
]