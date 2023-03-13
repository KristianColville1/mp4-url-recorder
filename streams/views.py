from django.shortcuts import render
from .models import Stream


def get_streams(request):
    all_streams = Stream.objects.all()
    context = {
        'streams': all_streams
    }
    return render(request, 'streams/index.html', context)