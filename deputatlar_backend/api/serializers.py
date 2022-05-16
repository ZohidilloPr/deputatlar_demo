from rest_framework import serializers
from app.models import Blogs

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ('id', 'lang', 'image', 'title', 'blog')