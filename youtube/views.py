from django.shortcuts import render
from pytube import YouTube

# Create your views here.
def download_video(request):
    video = request.POST.get('video')
    yt = YouTube(video).streams.first().download()
    return render(request, youtube.html, {})
