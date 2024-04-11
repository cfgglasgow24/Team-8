from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('home/', views.register, name='home'),
    path('test/', views.all_posts, name='test')
    # Include the URLs from myapp
]