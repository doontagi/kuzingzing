from rest_framework import serializers
from pimfy1.models import Post
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (,)