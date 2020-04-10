from django.shortcuts import render

# Create your views here.

def default_map(request):
    mapbox_access_token = 'pk.eyJ1IjoiaG9tYXlvdW4xOTkwIiwiYSI6ImNrOHU3d21ydTAyMXgzZnFreDVmcDN2dXgifQ.ArLQt1hviwq5AlWgwGs8bw'
    return render(request, 'default.html', 
                  { 'mapbox_access_token': mapbox_access_token })

