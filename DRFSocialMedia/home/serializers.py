from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='get_username')
    user_id = serializers.IntegerField(source='get_user_id')

    class Meta:
        model = User
        fields = ('username', 'user_id')

        read_only_fields = ('username', 'user_id')


class PostSerializer(serializers.ModelSerializer):
    posted_by = serializers.DictField(child=serializers.CharField(), source='get_user', read_only=True)
    pub_date = serializers.CharField(source='get_readable_date', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'posted_by', 'pub_date', 'text', 'in_reply_to_post']
        write_only_fields = ['text', 'in_reply_to_post']
