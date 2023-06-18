from django import forms
from .models import MusicFiles, ShareTo


class MusicFilesForms(forms.ModelForm):
    class Meta:
        model = MusicFiles
        fields = ['music_name','album_art','music_files','upload_type']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['album_art'].widget.attrs['accept'] = 'image/*'
        self.fields['music_files'].widget.attrs['accept'] = 'audio/*'
        

class ShareToForm(forms.ModelForm):
    class Meta:
        model = ShareTo
        fields = ['share_to',]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['share_to'].widget.attrs['placeholder'] = 'Enter a valid email address'
        
        
