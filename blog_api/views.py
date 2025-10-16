from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend  # new

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]  # new
    filterset_fields = ['author']  


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserPostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.kwargs['id']
        return Post.objects.filter(author=user)