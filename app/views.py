from django.shortcuts import render
from lists.utils import render_and_respond
from app.models import Sheet
import logging
logger = logging.getLogger('app-views')

# Create your views here.

def index(request):
    sheet = Sheet.objects.all()
    logger.info(sheet)
    return render_and_respond(request, 'app/index.html', {'sheet':sheet})

def addsheet(request):
    return render_and_respond(request, 'app/addsheet.html', {})
    