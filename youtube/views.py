from django.shortcuts import render, redirect
from youtube.forms import YouTubeForm, YouTube_add
from youtube.models import Youtube_file
from pytube import YouTube
from tempfile import TemporaryFile
import os
import shutil
from django.http import FileResponse, HttpResponse
import sweetify as swal


def delete_file(request):
    path = 'youtube/downloads/{}'.format(request.user)
    shutil.rmtree(path)


# Create your views here.
def download_video(request):
    history = Youtube_file.objects.filter(user=request.user)
    if request.method == 'POST':
        video = request.POST.get('url')
        yt = YouTube(video)
        data = {'title': yt.title, 'thumbnail': yt.thumbnail_url, 'url': video}
        form = YouTube_add(initial=data)
        model = Youtube_file(title=yt.title,
                            thumbnail=yt.thumbnail_url,
                            url=video)
        model.save()
        context = {'form': form, 'img':yt.thumbnail_url, 'video': video}     
        return render(request, 'youtube_info.html', context)
    else:
        form = YouTubeForm
        try:
            delete_file(request)
        except FileNotFoundError as error:
            print(error)
        context = {'form': form, 'history': history}
        return render(request, 'youtube.html', context)
    

def download(request):
    x = request.GET['url']
    video = YouTube(x)
    video.streams.first().download('youtube/downloads/{}/'.format(request.user))
    path = ('youtube/downloads/{}/{}.mp4'.format(request.user, video.title))
    with open(path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="video/mp4/force-download")
        response['Content-Disposition'] = 'attachment; filename=downloaded_video.mp4'
        return response

    


    


