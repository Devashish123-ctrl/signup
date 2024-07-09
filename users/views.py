from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login, authenticate,logout
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegistrationForm, PatientProfileForm, DoctorProfileForm


@csrf_exempt
def signup_patient(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save(commit=False)
        
            user.is_patient = True
            print(user)
            user.save()
            profile_form = PatientProfileForm(request.POST)
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            print(request.user)
            return redirect('dashboard')
        


    else:
        user_form = UserRegistrationForm()
        profile_form = PatientProfileForm() 
        return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(request.user)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')




def dashboard(request):
    print(request.user)
    if request.user.is_patient:
        profile = request.user.patientprofile
    elif request.user.is_doctor:
        profile = request.user.doctorprofile
    return render(request, 'dashboard.html', {'profile': profile})





def check(request):
      return render(request,'check.html')




@csrf_exempt
def signup_doctor(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)
        print(user_form.is_valid())
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user_form.save(commit=True)
            user.is_doctor = True
            user.save()
            print(request.user)
            profile_form = DoctorProfileForm(request.POST)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
            login(request, user)
            print(request.user)
            
            return redirect('dashboard')
        else:
            valid = user_form.is_valid
            print(valid)
            print(user_form.errors)
            return HttpResponse(valid)
    else:
        user_form = UserRegistrationForm()
        profile_form =  DoctorProfileForm()
        return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})



def logouts(request):
    print(request.user)
    logout(request)
    return redirect("/users/login")




