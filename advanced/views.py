from django.shortcuts import render

def get_advanced(request):
  return render(request, 'advanced/index.html')