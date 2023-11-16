from django.shortcuts import render
from django.http import HttpResponse
#add new import for user to fetch data from User table in a database
from .models import User

# Create your views here.
# def index(request):
#     return HttpResponse('Hello')

#add this code to run the html templates
def index(request):
    user_list = User.objects.order_by('pub_date')[:5] #use negative sign before the pubdate to descend order/ [:5] limit by 5
    context = {'user_list': user_list}
    
    return render(request, 'users/index.html', context) #context is added to pass the data
