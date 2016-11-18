from django.apps import AppConfig
from django.shortcuts import render
from .forms import UploadImageForm
# Create your views here.
from django.http import HttpResponse
from .models import Bild
from django.utils import timezone
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import StringIO, BytesIO
import PIL

import PIL.Image
import uuid
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile



def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UploadImageForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            upload_file = form.cleaned_data['file']
            basewidth = 500
            imagename = str(uuid.uuid4())
            img = PIL.Image.open(upload_file)
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            st = BytesIO()
            img.resize((basewidth, hsize), PIL.Image.ANTIALIAS).save(st, 'jpeg')
            processed_file = InMemoryUploadedFile(st, None, imagename, 'image/jpeg',
                                                  len(st.getvalue()), None)



            incepttext = "test"  # inception(image)
            usertext = form.cleaned_data.get('user_title')
            time = timezone.now()
            new_bild = Bild(file=processed_file,user_title=usertext,incept_title=incepttext,pub_date=time)
            new_bild.save()

    form = UploadImageForm()
    bilder= Bild.objects.order_by('-pub_date')
    return render(request, 'index.html',{'form':form,'bild_list':bilder})


def form_handle(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = UploadImageForm(request.POST,request.FILES)
        # check whether it's valid:
        image = request.FILES['file']
        incepttext = "test" #inception(image)
        usertext = "test"
        new_bild = Bild(image=image,user_title=usertext,incept_title=incepttext)
        new_bild.save()

