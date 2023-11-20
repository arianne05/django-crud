from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
#add new import for user to fetch data from User table in a database
from .models import User
#import for pagination functionality
from django.core.paginator import Paginator
#add new import for try and excepts function to work
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
# def index(request):
#     return HttpResponse('Hello')

#add this code to run the html index.html templates
def index(request):
    #previous code without pagination
    #user_list = User.objects.order_by('pub_date')[:] #use negative sign before the pubdate to descend order/ [:5] limit by 5
    #context = {'user_list': user_list}
    #return render(request, 'users/index.html', context) #context variable is added to pass its data

    #updated code with pagination
    user_list = User.objects.all().order_by('-id') #revised code to put pagination
    paginator = Paginator(user_list, 5)
    page_number = request.GET.get('page')
    user_list = paginator.get_page(page_number)
    return render(request, 'users/index.html', {'page_obj': user_list})
    

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

#function for getting the full details of a certain user
def detail(request, profile_id):
    try:
        user = User.objects.get(pk=profile_id)
    except User.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'users/detail.html', {'users':user}) #redirects to details.html and passing a 'user' variable/parameter

#function for delete
def delete(request, profile_id):
    User.objects.filter(id=profile_id).delete() #filter first which profiled id to delete
    return HttpResponseRedirect('/users') #retun to index.html

#function for displaying details in edit inside an input type
def edit(request, profile_id):
    try:
        user = User.objects.get(pk=profile_id)
    except User.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'users/edit.html', {'users':user})

#function to process update in edit
def processedit(request, profile_id):
    user = get_object_or_404(User, pk=profile_id) # import get_object_or_404 for checking if a certain id is avail in the database
    profile_pic = request.FILES.get('image')
    try:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        position = request.POST.get('position')
    except (KeyError, User.DoesNotExist): #partner by the get_object_or_404
        return render(request, 'profiles/detail.html', {
            'user':user,
            'error_message': "Problem updating record",})
    else:
        user_profile = User.objects.get(id=profile_id)
        user_profile.user_fname = fname
        user_profile.user_lname = lname
        user_profile.user_email = email
        user_profile.user_position = position
        if profile_pic:
            user_profile.user_image = profile_pic
        user_profile.save()
        return HttpResponseRedirect(reverse('users:detail', args=(profile_id,))) #must put reverse method
