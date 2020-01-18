from django.shortcuts import render
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
    try:
        prof = Profile.objects.get(user_id = user_id)
        posts = Project.objects.filter(profile_id = prof.id)
        for post in posts:
            name = post.title.split()
            if len(name) > 1:
                post.title = '_'.join(name)
            else:
                pass
    except Profile.DoesNotExist:
        posts = None
    
    try:
        businesses = Business.objects.all()
    except Business.DoesNotExist:
        businesses = None


    # username = user.get_username
    username = user.get_username()
    form = editForm()
    create_business = businessForm()
    create_neighbourhood = neighbourhoodForm()
    # if request.method == "POST":
    #     form = editForm(request.POST, request.FILES)
    #     create_form = createForm(request.POST, request.FILES)
    #     if form.is_valid() and create_form.is_valid():
    #         image = create_form.save(commit = False)
    #         profile = form.save(commit=False)
    #         profile.user = request.user
    #         image.profile_user = request.user
    #         profile.save()
    #         image.save()
            
    # else:
    #     form = editForm()
    #     create_form = createForm()

    try:
        
        profile = Profile.objects.get(user = user_id)
        # username = u.username
    except Profile.DoesNotExist:
        profile = None

    return render(request, 'profile.html', {'form': form, 'businesses': businesses, 'create_business': create_business, 'profile': profile, 'username': username, 'user': user})


def update_profile(request):
    if request.method == 'POST':
        
        form = editForm(request.POST, request.FILES)
        if form.is_valid():
            usr = request.user
            Profile.objects.filter(user_id=usr.id).delete()
            # photo = request.POST['photo']
            # bio = request.POST['bio']
            # profile = Profile.objects.filter(user_id = request.user.id).update(photo = photo, bio = bio)
            profile = form.save(commit = False)
            profile.user = request.user
            profile.save()
            return redirect('profile', user_id = request.user.id)