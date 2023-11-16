from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse('Hello')

#add this code to run the html templates
def index(request):
    return render(request, 'users/index.html')
