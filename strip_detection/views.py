from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .utils import strip_detection
# Create your views here.
class StripDetectectionViewset(ViewSet):
    def create(self, request):
        print(request.FILES)
        image = request.FILES['image']
        res_dict = strip_detection(image)
        return Response(res_dict)