from django.urls import path
from first_app.views import hello , contact_view

urlpatterns = [
    path('hello/' , hello),
    path('contact_view/' , contact_view , name = 'contact'),
]