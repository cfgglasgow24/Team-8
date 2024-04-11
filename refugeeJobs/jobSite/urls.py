from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),# Include the URLs from myapp
    path('home/', views.register, name='home'),
    path('test/', views.all_posts, name='test'),
]