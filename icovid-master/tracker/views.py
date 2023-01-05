from django import forms
from django.http import response
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from .forms import FilterForm
from .models import TrackerFilter
from .utils import request_schema
from . import schema as schema

# Create your views here.
def index(request):
    response = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FilterForm(request.POST)
            if form.is_valid():
                chartType = form.cleaned_data['chart_type']
                numberOfData = form.cleaned_data['number_of_data']
                tmp = TrackerFilter(user=request.user, chart_type=chartType, number_of_data=numberOfData)
                tmp.save()
                return HttpResponseRedirect(reverse("index"))
        else:
            if not hasattr(request.user, 'trackerfilter'):
                tmp = TrackerFilter(user=request.user, chart_type=1, number_of_data=7)
                tmp.save()
        tmp = TrackerFilter.objects.get(user=request.user)
        response = {
            "number_of_data" : tmp.number_of_data,
            "chart_type" : tmp.chart_type,
            "form" : FilterForm({
                'chart_type' : tmp.chart_type,
                "number_of_data" : tmp.number_of_data
            })
        }
    else:
        response = {"number_of_data" : 7, "chart_type" : 1, "form" : FilterForm()}
    
    return render(request, "tracker_index.html", response)

# API for mobile apps
@csrf_protect
@request_schema(method='POST', schema=schema.update_filter_api_request)
def updateFilterApi(request, data):
    if request.is_ajax:
        tmp = TrackerFilter(user=request.user, chart_type=int(data['chart_type']), number_of_data=int(data['number_of_data']))
        tmp.save()
        return JsonResponse(status=200, data={'message': 'Saved Successfully'})

    return JsonResponse(status=500, data={'message': 'Internal Server Error'})

@csrf_protect
@request_schema(method='POST', schema=schema.get_filter_api_request)
def getFilterApi(request, data):
    if request.is_ajax:
        if not hasattr(request.user, 'trackerfilter'):
            tmp = TrackerFilter(user=request.user, chart_type=1, number_of_data=7)
            tmp.save()
        tmp = TrackerFilter.objects.get(user=request.user)
        return JsonResponse(status=200, data={'message': 'Loaded Successfully', 'chart_type': tmp.chart_type, 'number_of_data': tmp.number_of_data})

    return JsonResponse(status=500, data={'message': 'Internal Server Error'})