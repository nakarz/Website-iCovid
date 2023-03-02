# Create your views here.
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Announcement
from .forms import AnnouncementForm
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def make_announcement(request):
    form = AnnouncementForm(request.POST or None)

    if (request.method == 'POST'):
        if (form.is_valid):
            form.save()

            return HttpResponseRedirect("/administrator/")
        
    response = {'form': form}
    return render(request, 'utilities_make_announcement.html', response)

@user_passes_test(lambda u: u.is_superuser)
def get_announcement(request):
    announcement = Announcement.objects.all()
    
    data = serializers.serialize('json', announcement)        
    return HttpResponse(data, content_type="application/json")

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

@user_passes_test(lambda u: u.is_superuser)
def see_log(request):
    log_file = open(BASE_DIR/'utilities/log/icovid_log.log','r')
    log_content_dirty = log_file.readlines()
    log_content = [line.strip() for line in log_content_dirty]
    log_file.close()

    response = {'log_content': log_content}
    return render(request, 'utilities_see_log.html', response)

