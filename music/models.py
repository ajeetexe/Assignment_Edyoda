from django.db import models
from account.models import User
# Create your models here.

class MusicFiles(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    music_name = models.CharField(max_length=1000)
    album_art = models.ImageField(upload_to='media/albumArt')
    music_files = models.FileField(upload_to='media/musicFiles')
    uploaded_on = models.DateTimeField(auto_now_add=True)
    upload_type = models.CharField(max_length=100,choices=(
        ('public','Public'),
        ('private','Private'),
        ('protected','Protected')
    ))
    def __str__(self):
        return str(self.uploaded_on)

class ShareTo(models.Model):
    music_id = models.ForeignKey(MusicFiles,models.CASCADE)
    share_by = models.ForeignKey(User,models.CASCADE)
    share_to = models.EmailField()
    share_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.share_to)