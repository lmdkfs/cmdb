from django.shortcuts import render_to_response
from web_manage.forms.account import LoginForm

# Create your views here.

def index(request):
    login_form = LoginForm(request.POST)
    return render_to_response('home/index.html', {'model':login_form})
