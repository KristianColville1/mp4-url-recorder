from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Stream
from django.contrib import messages
from django.db.models import Q

def get_streams(request):
    all_streams = Stream.objects.all()
    query = None
    
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect('/streams/')

            queries = Q(name__icontains=query)
            all_streams = all_streams.filter(queries)
    context = {
        'streams': all_streams
    }
    return render(request, 'streams/index.html', context)