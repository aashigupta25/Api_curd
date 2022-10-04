from msilib.schema import ServiceInstall
from django.shortcuts import render
import io
from django.urls import is_valid_path
from requests import request
from rest_framework.parsers import JSONParser
from .models import APIoperation
from .serializer import APIoperationSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def Operation_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            Api = APIoperation.objects.get(id = id)
            serializer= APIoperationSerializer(Api)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')
        
        Api = APIoperation.objects.all()
        serializer = APIoperationSerializer(Api, many= True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')

if request.method == 'POST':
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    serializer = APIoperationSerializer(data = pythondata)
    if serializer.is_valid():
        serializer.save()
        res = {'msg' :'Data Created'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type = 'application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type= 'application/json')