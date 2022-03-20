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
    police = Police.objects.filter(neighbourhood = occupant.neighbourhood.id).all()
    businesses = Businesses.objects.filter(neighbourhood = occupant.neighbourhood.id).all()
    posts = Posts.objects.filter(neighbourhood = occupant.neighbourhood.id).all()
    return render(request, 'home.html', {"current_user":current_user, "neighbourhoods":neighbourhoods, "police":police, "businesses":businesses, "posts":posts})

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

def view_neighborhood(request, id):
    neighbourhood = Neighbourhood.objects.filter(pk = id).first()
    police = Police.objects.filter(neighbourhood = neighbourhood).all()
    HealthCareCenter = HealthDepartment.objects.filter(neighbourhood = neighbourhood).all()

    context = {
        "neighborhood": neighbourhood,
        "police": police,
        "healthcareCenter": HealthCareCenter
    }

    return render(request, 'neighbourhood.html', context )

def create_post(request):
    current_user = request.user  
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

    return render(request, 'post.html', {"form":form})     
