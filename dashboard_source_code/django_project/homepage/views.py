from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            message1 = 'Please try one more time.'
            messages.success(request, message1)
    return render_to_response('login.html', context_instance=RequestContext(request))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def home(request):
    return render_to_response("home.html", locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def aboutus(request):
    return render_to_response("aboutus.html", locals(), context_instance=RequestContext(request))