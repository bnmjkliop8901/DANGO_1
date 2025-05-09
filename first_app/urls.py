from django.urls import path
from first_app.views import hello

urlpatterns = [
    path('hello/' , hello)
]