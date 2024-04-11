from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in directly after registration
            return redirect('home')  # Redirect to a home page or dashboard
    else:
        form = CustomUserCreationForm()
    return render(request, 'jobSite/register.html', {'form': form})
