from django.shortcuts import render
from lists.utils import render_and_respond
from app.models import Sheet

# Create your views here.

def index(request):
    sheet = Sheet.objects.all()
    return render_and_respond(request, 'app/index.html', {'sheet':sheet})
    