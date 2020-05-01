from django.shortcuts import render
from .models import Records

# Create your views here.
def details(request, id):
    record = Records.objects.get(id=id)
    context = {
        'record' : record
    }
    return render(request, 'details.html', context)