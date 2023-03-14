from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Stream
from django.contrib import messages
from django.db.models import Q
from .stream_calander import get_calander_days_of_month, DAYS


def get_streams(request):
    """
    Gets all the streams and shows them in the front end.
    If the request method is GET it will search the stream
    objects for the query selected by a user.
    """
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
    all_streams = all_streams.order_by('name')
    context = {
        'streams': all_streams
    }
    return render(request, 'streams/index.html', context)


def get_stream_detail(request, stream_name):
    """
    Gets the details of the stream selected in the front end
    """
    stream = Stream.objects.filter(name=stream_name)
    stream = stream.last()
    
    previous_month = get_calander_days_of_month(2,2023)
    present_month = get_calander_days_of_month(3, 2023)
    
    context = {
        'stream': stream,
        'previous_month_dict': previous_month,
        'present_month_dict': present_month,
        'this_month': 'March',
        'last_month': 'February',
        'days': DAYS,
    }
    return render(request, 'streams/stream_detail.html', context)