from django.shortcuts import render
from lists.utils import render_and_respond
from app.models import Sheet
from datetime import datetime
import logging
logger = logging.getLogger('app-views')

# Create your views here.

def index(request):
    sheet = Sheet.objects.all()
    logger.info(sheet)
    return render_and_respond(request, 'app/index.html', {'sheet':sheet})

def addsheet(request):
    if request.method == 'POST':
        logger.info("post yes")
        name = request.POST['name'] if 'name' in request.POST else None
        date = request.POST['date'] if 'date' in request.POST else datetime.utcnow()
    return render_and_respond(request, 'app/addsheet.html', {})
    