from django.shortcuts import render, redirect
from .forms import SubmitFormData
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = SubmitFormData(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             sex = form.cleaned_data['sex']
#             goal = form.cleaned_data['goal']
#             experience = form.cleaned_data['experience']
#             age = form.cleaned_data['age']
#             city = form.cleaned_data['city']
#             gym_membership = form.cleaned_data['gym_membership']
#             user = user_data(name=name, age=age, sex=sex, goal=goal,experience=experience, city=city, gym_membership=gym_membership )
#             user.save()
#             return redirect(search)
#     else:
#         form = SubmitFormData()
#     return render(request, 'register.html', {'form': form})
    # return render(request, 'home_index.html')