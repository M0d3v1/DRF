from django.urls import path, include

urlpatterns = [
    # Other URL patterns for your project
    path('', include('todo.urls')),
]
