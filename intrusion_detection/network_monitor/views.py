

from django.shortcuts import render

def index(request):
    return render(request, 'network_monitor/index.html')  # Make sure this template exists
