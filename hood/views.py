from django.shortcuts import render, redirect
from .forms import editForm, businessForm, neighbourhoodForm, MyCustomLoginForm, MyCustomSignupForm, MyCustomSetPasswordForm
from .models import Profile, Neighbourhood, Business

# Create your views here.
def home(request):
    return render(request, 'index.html')


def login(request):
    form = MyCustomLoginForm()
    return render(request, 'account/login.html', {'form':form})

def signup(request):
    form = MyCustomSignupForm()
    return render(request, 'account/signup.html', {'form':form})



def profile(request, user_id):
    user = request.user
    # try:
    #     prof = Profile.objects.get(user_id = user_id)
    #     posts = Project.objects.filter(profile_id = prof.id)
    #     for post in posts:
    #         name = post.title.split()
    #         if len(name) > 1:
    #             post.title = '_'.join(name)
    #         else:
    #             pass
    # except Profile.DoesNotExist:
    #     posts = None
    try:
        
        profile = Profile.objects.get(user_id = request.user.id)
        try:
            neighbourhood = Neighbourhood.objects.get(pk = profile.neighbourhood_id)
        except Neighbourhood.DoesNotExist:
            neighbourhood = None
        
    
        try:
            businesses = Business.objects.filter(neighbourhood_id = neighbourhood.id)
            for business in businesses:
                biz_name = business.name.split(" ")
                if len(biz_name) > 1:
                    business.name = '_'.join(biz_name)
                else:
                    pass
        except Business.DoesNotExist:
            businesses = None
        # username = u.username
    except Profile.DoesNotExist:
        profile = None
        businesses = None


    


    # username = user.get_username
    username = user.get_username()
    form = editForm()
    create_business = businessForm()
    create_neighbourhood = neighbourhoodForm()

    

    return render(request, 'profile.html', {'form': form, 'businesses': businesses, 'create_business': create_business, 'profile': profile, 'username': username, 'create_neighbourhood': create_neighbourhood})


def update_profile(request):
    if request.method == 'POST':
        
        form = editForm(request.POST, request.FILES)
        if form.is_valid():
            usr = request.user
            # neighbourhood = Neighbourhood.objects.get()
            Profile.objects.filter(user_id=usr.id).delete()
            # photo = request.POST['photo']
            # bio = request.POST['bio']
            # profile = Profile.objects.filter(user_id = request.user.id).update(photo = photo, bio = bio)
            profile = form.save(commit = False)
            profile.user = request.user
            profile.save()
            return redirect('profile', user_id = request.user.id)

def create_post(request):
    profile = Profile.objects.get(user = request.user.id)
    form = businessForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save(commit = False)
        post.neighbourhood_id = profile.neighbourhood_id
        post.profile_id = profile.id
        post.save()
        print("post has been created")
    return redirect('profile', user_id = request.user.id)

def change(request):
    form = neighbourhoodForm(request.POST)
    if form.is_valid():
        neighbourhood = request.POST['name']
        hood = Neighbourhood.objects.get(id = neighbourhood)
        
        Profile.objects.filter(user_id = request.user.id).update(neighbourhood_id = hood.id)
        
    return redirect('profile', user_id = request.user.id)

def search(request):
    search_term = request.POST['search']
    try:
        businesses = Business.objects.filter(name = search_term)
    except Business.DoesNotExist:
        businesses = None

    return render(request, 'search.html', {'businesses': businesses, 'search_term': search_term})