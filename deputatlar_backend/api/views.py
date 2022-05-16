from django.shortcuts import render
from app.models import  Blogs
from .serializers import BlogSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class BlogList(ListCreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer

class BlogDetail(RetrieveUpdateDestroyAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer