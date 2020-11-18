from django.shortcuts import render, redirect
from youtube.forms import YouTubeForm, YouTube_add
from youtube.models import Youtube_file
from pytube import YouTube
from tempfile import TemporaryFile
import os
from django.http import FileResponse, HttpResponse
import sweetify as swal

# Create your views here.
def download_video(request):
    if request.method == 'POST':
        video = request.POST.get('url')
        yt = YouTube(video)
        data = {'title': yt.title, 'thumbnail': yt.thumbnail_url}
        form = YouTube_add(initial=data)
        model = Youtube_file(title=yt.title,
                            thumbnail=yt.thumbnail_url,
                            url=video)
        model.save()
        context = {'form': form, 'img':yt.thumbnail_url, 'video': video}     
        return render(request, 'youtube_info.html', context)
    else:
        form = YouTubeForm
        context = {'form': form }
        return render(request, 'youtube.html', context)
    

def download(request):
    x = request.GET['url']
    video = YouTube(x)
    video.streams.first().download('youtube/downloads/{}/'.format(request.user))
    dir = ('youtube/downloads/{}/{}.mp4'.format(request.user, video.title))
    response2 = redirect('/youtube')
    with open(dir, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="video/mp4/force-download")
        response['Content-Disposition'] = 'attachment; filename={}.mp4'.format(video.title)
        return response

    
def delete_file(request):
    os.remove('youtube/downloads/{}/{}.mp4'.format(request.user, video.title))
    resp = swal.sucess(request, text='deletado')
    return resp


