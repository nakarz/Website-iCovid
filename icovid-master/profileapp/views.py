from collections import namedtuple
import json
from os import name
from typing import BinaryIO
from django.contrib.auth.models import User
from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from profileapp.forms import ProfileUpdateForm, UserUpdateForm
from profileapp.models import Profile
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def profile(request):
    return render(request, 'main_profile.html')
    
@login_required
def profileupdate(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # profilelist = []
            # data_dict = {}
            # data_dict['name'] = request.POST.get('name')
            # data_dict['avatar'] = request.POST.get('avatar')
            # data_dict['email'] = request.POST.get('email')
            # data_dict['phone'] = request.POST.get('phone')
            # data_dict['city'] = request.POST.get('city')
            # data_dict['bio'] = request.POST.get('bio')
            # data_dict['status'] = request.POST.get('status')
            # data_dict['vaccinated_status'] = request.POST.get('vaccinated_status')
            # profilelist.append(data_dict)
            # return JsonResponse(data_dict, safe=False)
            return redirect('user-profile')
        return redirect('user-profile')
        #     messages.success(request, ('Your profile has been updated!'))
        # else:
        #     messages.error(request, ('Unable to update your profile'))
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form,
    }

    return render(request, 'edit_profile.html', context)

# other user
@login_required
def otheruserprofile(request, id):
    user = User.object.get(name=id)
    return render(request,'other_profile.html', {'user': user})

def profiledatas(request):
    form = Profile.objects.all()
    data = serializers.serialize('json', form)
    return HttpResponse(data, content_type="applications/json")