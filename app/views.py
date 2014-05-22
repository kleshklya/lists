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
    logger.info('nya')
    if request.method == 'POST':
        logger.info("post yes")
        name = request.POST['name'] if 'name' in request.POST else None
        logger.info(name)
        date = request.POST['date'] if 'date' in request.POST else datetime.utcnow()
        date = datetime.strptime(date, '%m/%d/%Y %I:%M %p')
        logger.info(date)
        sheet = Sheet()
        sheet.name = name
        sheet.date = date
        sheet.save()
        logger.info('Sheet created: id is %s and name is "%s".' % (sheet.id, sheet.name))
        sheet_created = True
        return render_and_respond(request, 'app/addsheet.html', {'sheet_created': sheet_created})
    return render_and_respond(request, 'app/addsheet.html', {})

def allsheets(request):
    allsheets = Sheet.objects.all()
    logger.info(allsheets)
    return render_and_respond(request, 'app/allsheets.html', {'view_sheets': allsheets})
    