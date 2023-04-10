from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
from django.http import JsonResponse


class PostListView(APIView):

    def get(self, request):
        post = Post.objects.filter(in_reply_to_post=None)
        srz_data = PostSerializer(instance=post, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


class CommentList(generics.ListAPIView):  # turn this into a method in postviewset
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(in_reply_to_post=self.kwargs["pk"])


class PostList(generics.ListAPIView):  # turn this into a method in postviewset
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(posted_by=self.kwargs["pk"], in_reply_to_post=None)


class PostCreateView(APIView):
    """
        Create a new post
    """
    permission_classes = [IsAuthenticated, ]
    serializer_class = PostSerializer

    def post(self, request):
        srz_data = PostSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class PostLikeView(generics.ListAPIView):  # turn this into a method in postviewset
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(liked_by=self.kwargs["pk"])


class PostRateViewSet(generics.GenericAPIView): # use mixins instead
    srz_cls = PostSerializer

    def get(self, request, pk):
        post_rating = Post.objects.update(id=pk, liked_by=request.user)
        post_rating.save()
        return Response(post_rating.data, status=status.HTTP_201_CREATED)
