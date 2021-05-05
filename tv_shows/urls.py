from django.urls import path, include

urlpatterns = [
    path('shows/', include('tv_shows_app.urls')),
]
