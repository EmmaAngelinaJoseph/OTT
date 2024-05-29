from django.db.models import Q
from django.forms import models
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .forms import MyLoginForm, UserRegisterForm, MovieForm
from django.http import HttpResponse, JsonResponse

from .models import UserProfile, movies


# from .models import UserProfile


# Create your views here.
def adminindex(request):
    return render(request, 'adminbase.html')

def user_login(request):
    if request.method == 'POST':
        login_form = MyLoginForm(request.POST)
        if login_form.is_valid():
            cleaned_data = login_form.cleaned_data
            auth_user = authenticate(request, username=cleaned_data['username'],
                                     password=cleaned_data['password'])
            if auth_user is not None:
                login(request, auth_user)
                return HttpResponse('Authenticated')
    else:
        login_form = MyLoginForm()
    return render(request, 'useraccount/login_form.html',
                  {'login_form': login_form})
def register(request):
    if request.method=='POST':
        user_reg_form=UserRegisterForm(request.POST)
        if user_reg_form.is_valid():
            new_user=user_reg_form.save(commit=False)
            new_user.set_password(user_reg_form.cleaned_data['password'])
            new_user.save()
            return render(request,'registration/register_done.html',{'user_reg_form':user_reg_form})
    else:
        user_reg_form=UserRegisterForm()
    return render (request,'registration/register.html',
                   {'user_reg_form':user_reg_form})
# views.py


def customer_list(request):
    query = request.GET.get('q')
    if query:
        users = UserProfile.objects.filter(
            Q(user__username__icontains=query) |
            Q(user__email__icontains=query) |
            Q(user__mobile__icontains=query)
        )
    else:
        users = UserProfile.objects.all()
    return render(request, 'customer_list.html', {'users': users})
def movie_list(request):
    query = request.GET.get('q')
    if query:
        movies_list = movies.objects.filter(
            Q(title__icontains=query) |
            Q(main_actor__icontains=query) |
            Q(director__icontains=query)
        )
    else:
        movies_list = movies.objects.all()
    return render(request, 'movie_list.html', {'movies': movies_list})
def upload_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'upload_movie.html', {'form': form})

def delete_movie(request, id):
    movie = get_object_or_404(movies, id=id)
    if request.method == 'DELETE':
        movie.delete()
        return JsonResponse({'message': 'Movie deleted successfully.'}, status=200)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

def toggle_disable_movie(request, id):
    movie = get_object_or_404(movies, id=id)
    if request.method == 'POST':
        movie.disabled = not movie.disabled
        movie.save()
        return JsonResponse({'message': 'Movie status updated successfully.'}, status=200)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)