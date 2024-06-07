from django.urls import path
from .views import StripDetectectionViewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'strip', StripDetectectionViewset, basename='strip')
urlpatterns = []
urlpatterns += router.urls