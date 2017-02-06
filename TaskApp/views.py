# from open_facebook import OpenFacebook
from rest_framework import generics
from rest_framework_mongoengine.generics import ListCreateAPIView

from .serializers import *
from .models import *


class UserDetail(generics.CreateAPIView):
    serializer_class = UserSerializer
