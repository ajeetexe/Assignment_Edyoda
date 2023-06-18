from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('upload-music/',upload_music,name='upload-music'),
    path('protected-view/<id>/',protected_view,name='protected-view'),
    path('my-upload/',my_upload,name='my-upload'),
]
