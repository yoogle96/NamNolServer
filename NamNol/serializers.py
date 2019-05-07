from rest_framework import serializers
from NamNol.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        # fields = ('title')
        fields = "__all__"