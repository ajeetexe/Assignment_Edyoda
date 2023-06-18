from django.shortcuts import render,redirect
from .forms import MusicFilesForms, ShareToForm
from account.models import User
from music.models import MusicFiles, ShareTo
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/account/login/')
def index(request):
    user = User.objects.filter(username=request.user).first()
    music = MusicFiles.objects.all()
    music_list = []
    for m in music:
        # print(m.upload_type)
        if m.upload_type == 'public':
            music_list.append(m)
        if m.upload_type == 'private' and m.user == user:
            music_list.append(m)
        if m.upload_type == 'protected':
            share_obj = ShareTo.objects.filter(music_id=m.pk).first()
            if share_obj:
                if share_obj.share_to == str(user) or share_obj.share_by == user:
                    music_list.append(m)

    
    return render(request,'index.html',context={'music_list':music_list})


@login_required(login_url='/account/login/')
def upload_music(request): 
    form = MusicFilesForms()
    if request.method == 'POST':
        form = MusicFilesForms(request.POST,request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = User.objects.filter(username = request.user).first()
            form.save()
            if f.upload_type == 'protected':
                return redirect(f'/protected-view/{f.pk}/')
            else:
                return redirect('/')
    return render(request,'upload-music.html',context={'form':form})

@login_required(login_url='/account/login/')
def protected_view(request,id):
    user_list = [x.username for x in User.objects.all()]
    form = ShareToForm()
    if request.method == 'POST':
        form = ShareToForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.music_id = MusicFiles.objects.filter(pk=id).first()
            f.share_by = User.objects.filter(username=request.user).first()
            if f.share_to not in user_list:
                messages.error(request,'User not registered')
                return redirect(f'/protected-view/{id}/')
            form.save()
            return redirect(f'/protected-view/{id}/')
    context = {
        'form':form,
        'music':MusicFiles.objects.filter(pk=id).first(),
        'share':ShareTo.objects.filter(music_id=MusicFiles.objects.filter(pk=id).first())
    }
    return render(request,'protected-view.html',context=context)

@login_required(login_url='/account/login/')
def my_upload(request):
    try:
        music_obj = MusicFiles.objects.filter(user=request.user)
    except Exception as e:
        print(e)
    return render(request,'my-upload.html',context={'music':music_obj})