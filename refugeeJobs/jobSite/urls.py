from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('posts/', views.all_posts, name='posts'),
    path('employer',views.employer, name="employer"),
    # Include the URLs from myapp
]