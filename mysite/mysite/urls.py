from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Include URLs from myapp
    path('polls/', include('polls.urls')),  # Include URLs from polls app
]
