from django.shortcuts import render
from first_app.forms import ContactForm  , ContactUsForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


def hello(request):
    context = {
        'username':'soheil',
        'skills':['p' , 'd' , 'f'],
        'show_skills':False,
    }
    return render(request , 'greetings/home.html' , context)

def contact_view(request):
    print(f"the method is :{request.method}")
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request , "thank you for submission")
            
        else:
            messages.error(request , "you have error on your form")
        return HttpResponseRedirect(reverse('contact'))
    
    else:   
        form = ContactUsForm()
        return render(request , 'greetings/contact_us.html' , {'form':form})
