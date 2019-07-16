from django.shortcuts import render
from .models import Assesment, Subjects
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'rfid/index.html')

def assesment(request):
    count=Assesment.objects.all().count()
    obj=Assesment.objects.all()
    data=[]
    if count <= 0 :
        messages.error(request,('There is no data in Assesment!'))
        return render(request, 'rfid/index.html')
    else:
        for i in obj:
            dataum={
                'assid':i.ass_id,
                'type':i.type,
                'date':i.date,
                'subid':i.sub_id,
            }
            data.append(dataum)
        return render(request,'rfid/index.html', {'data':data})



