from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from youtube.forms import YouTubeForm, YouTube_add
from youtube.models import Youtube_file
from pytube import YouTube
from tempfile import TemporaryFile
import os
import shutil
from django.http import FileResponse, HttpResponse
import sweetify as swal


@login_required
def delete_file(request):
    path = 'youtube/downloads/tmp'
    shutil.rmtree(path)


@login_required
def download_video(request):
    history = Youtube_file.objects.filter(user=request.user.id).reverse()
    paginator = Paginator(history, 4)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'POST':
        video = request.POST.get('url')
        try:
            yt = YouTube(video)
        except error:
            print(error)
        data = {'title': yt.title, 'thumbnail': yt.thumbnail_url, 'url': video}
        form = YouTube_add(initial=data)
        model = Youtube_file(title=yt.title,
                                thumbnail=yt.thumbnail_url,
                                url=video)
        model.user = request.user
        model.save()
        context = {'form': form, 'img':yt.thumbnail_url, 'video': video}     
        return render(request, 'youtube_info.html', context)
    else:
        form = YouTubeForm
        try:
            delete_file(request)
        except FileNotFoundError as error:
            print(error)
        context = {'history':history, 'form': form, 'page':page, 'posts':posts}
        return render(request, 'youtube.html', context)
    


@login_required
def download(request):
    x = request.POST.get('url')
    video = YouTube(x)
    video.streams.first().download('youtube/downloads/tmp/', filename='video')
    path = ('youtube/downloads/tmp/video.mp4')
    with open(path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="video/mp4/force-download")
        response['Content-Disposition'] = 'attachment; filename=downloaded_video.mp4'
        print('ola')
        return response



@login_required
def download_only_audio(request):
    x = request.POST.get('url')
    audio = YouTube(x)
    audio.streams.filter(only_audio=True).first().download('youtube/downloads/tmp/', filename='audio')
    path = ('youtube/downloads/tmp/audio.mp4')
    with open(path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="audio/mp3/force-download_only_audio")
        response['Content-Disposition'] = 'attachment; filename=downloaded_audio.mp3'
        return response
    


    


