from django.shortcuts import render

# Create your views here.


def hello(request):
    context = {
        'username':'soheil',
        'skills':['p' , 'd' , 'f'],
        'show_skills':False,
    }
    return render(request , 'greetings/home.html' , context)
