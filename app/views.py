from django.shortcuts import render
from lists.utils import render_and_respond

# Create your views here.

def index(request):
    return render_and_respond(request, 'app/index.html', {})