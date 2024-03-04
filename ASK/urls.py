
from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('front_desk.urls')),  # Include the URL patterns from the front_desk app
]


 