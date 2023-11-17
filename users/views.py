from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#add new import for user to fetch data from User table in a database
from .models import User
#add new import for try and excepts function to work
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
# def index(request):
#     return HttpResponse('Hello')

#add this code to run the html index.html templates
def index(request):
    user_list = User.objects.order_by('pub_date')[:] #use negative sign before the pubdate to descend order/ [:5] limit by 5
    context = {'user_list': user_list}
    
    return render(request, 'users/index.html', context) #context variable is added to pass its data

#add this code to run the html add.html templates
def add(request):
    return render(request, 'users/add.html')

#add this code to process the POST method
def processadd(request):
    fname = request.POST.get('fname') #the name set in the input type in html
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    position = request.POST.get('position')

    #for image we create a default image condition
    if request.FILES.get('image'):
        user_pic = request.FILES.get('image')
    else:
        user_pic = 'profile_pic/image.jpg'

    #create a try and except to check if email already exist
    try:
        n = User.objects.get(user_email=email)
        #email already exist
        return render(request, 'users/add.html', {'error_message':"Email already exist: " + email})
    
    except ObjectDoesNotExist:
        user = User.objects.create(user_email=email, user_fname=fname, 
                    user_lname=lname, user_position=position, user_image=user_pic)
        user.save() #insert data into the database
        return HttpResponseRedirect('/users') #after inserting into the database redirects into the previous page

