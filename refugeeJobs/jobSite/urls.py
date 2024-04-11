from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register , name='register'),# Include the URLs from myapp
]