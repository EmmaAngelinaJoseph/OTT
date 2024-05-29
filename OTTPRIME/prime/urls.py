from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import adminindex, register, customer_list, movie_list, upload_movie, delete_movie, toggle_disable_movie

urlpatterns = [
    path('registration/register',register,name='register'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('customer_list/', customer_list, name='customer_list'),
    path('movie_list/', movie_list, name='movie_list'),
    path('delete_movie/<int:id>/', delete_movie, name='delete_movie'),
    path('toggle_disable_movie/<int:id>/', toggle_disable_movie, name='toggle_disable_movie'),
    path('upload_movie/', upload_movie, name='upload_movie'),
    path('adminbase/', adminindex, name='adminindex')
]