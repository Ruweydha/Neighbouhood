from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import OccupantsForm, PostsForm
from .models import Neighbourhood, Occupants, Police, HealthDepartment, Businesses, Posts

# # Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    neighbourhoods = Neighbourhood.objects.all()
    current_user = request.user
    occupant = Occupants.objects.filter(user = current_user).first()
    if not occupant:
        return redirect("registerOccupants")
    else:
        police = Police.objects.filter(neighbourhood = occupant.neighbourhood.id).all()
        health_Department = HealthDepartment.objects.filter(neighbourhood = occupant.neighbourhood.id).all()
        businesses = Businesses.objects.filter(neighbourhood = occupant.neighbourhood.id).all()
        posts = Posts.objects.filter(neighbourhood = occupant.neighbourhood.id).all()
        print (posts)
       
    return render(request, 'home.html', {"current_user":current_user, "neighbourhoods":neighbourhoods, "police":police, "businesses":businesses, "posts":posts, "occupant":occupant, "healthDepartment":health_Department})

@login_required(login_url='/accounts/login/')
def register_occupant(request):
    current_user = request.user
    if request.method == 'POST':
        form = OccupantsForm(request.POST, request.FILES)
        
        if form.is_valid():
            occupant = form.save(commit = False)
            occupant.user = current_user
            occupant.save()
        return redirect("home")     
    else:
        form = OccupantsForm()   

    context = {
        "current_user":current_user,
        "form": form
    } 
    return render(request, 'occupants.html',context)    

@login_required(login_url='/accounts/login/')
def view_neighborhood(request, id):
    current_user = request.user
    neighbourhood = Neighbourhood.objects.filter(pk = id).first()
    neighbourhoods = Neighbourhood.objects.all()
    police = Police.objects.filter(neighbourhood = neighbourhood).all()
    HealthCareCenter = HealthDepartment.objects.filter(neighbourhood = neighbourhood).all()
    occupants = Occupants.objects.filter(neighbourhood = neighbourhood).all()

    context = {
        "neighborhood": neighbourhood,
        "police": police,
        "healthcareCenter": HealthCareCenter,
        "current_user":current_user,
        "occupants":occupants,
        "neighbourhoods":neighbourhoods

    }

    return render(request, 'neighbourhood.html', context )

@login_required(login_url='/accounts/login/')
def create_post(request):
    current_user = request.user 
    neighbourhoods = Neighbourhood.objects.all()
    occupant = Occupants.objects.filter(user = current_user).first()  
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = current_user
            post.neighbourhood = occupant.neighbourhood 
            post.save()
        return redirect("home")     
    else:
        form = PostsForm()   

    return render(request, 'post.html', {"form":form, "neighbourhoods":neighbourhoods})     

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user  
    neighbourhoods = Neighbourhood.objects.all()
    occupant = Occupants.objects.filter(user = current_user).first()  
    neighbourhood = Neighbourhood.objects.filter(pk = occupant.neighbourhood.id).first()
    police = Police.objects.filter(neighbourhood = neighbourhood).all()
    HealthCareCenter = HealthDepartment.objects.filter(neighbourhood = neighbourhood).all()
    occupants = Occupants.objects.filter(neighbourhood = neighbourhood).all()

    context = {
        "neighborhood": neighbourhood,
        "police": police,
        "healthcareCenter": HealthCareCenter,
        "current_user":current_user,
        "occupants":occupants,
        "occupant":occupant,
        "neighbourhoods":neighbourhoods

    }

    return render(request, 'profile.html', context)

@login_required(login_url='/accounts/login/')
def search_business(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Businesses.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"businesses": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})    